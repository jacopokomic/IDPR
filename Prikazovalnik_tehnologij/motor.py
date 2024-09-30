from __future__ import print_function
from sys import version_info
from time import sleep
from daqhats import mcc152, OptionFlags, HatIDs, HatError, DIOConfigItem
from daqhats_utils import select_hat_device

# -----------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    options = OptionFlags.DEFAULT
    address = select_hat_device(HatIDs.MCC_152)
    hat = mcc152(address)
    
    channel3 = 3
    channel7 = 7
    DIO3 = 0
    AO1 = 5.0
    
    rpm = float(input("\nizberi hitrost (0-3000 rpm): "))
    dolgo = float(input("0 - po 10 s\n1 - se ne ustavi\nkdaj se motor ustavi: "))
    
    if rpm < 0 or rpm > 3000 or dolgo not in [0, 1]:
        print("\n\tnapaka\n")
        exit()
    else:
        if rpm > 400:
            DIO7 = 1
            AO0 = (rpm/6000)*5
        else:
            DIO7 = 0
            AO0 = (rpm/400)*5
    
    val = [AO0, AO1]
    
    print("\n\tDIO3:", DIO3, "5 s, potem 5 s na 1\n\tDIO7:", DIO7, "\n\tAO0:", AO0, "V\n\tAO1:", AO1, "V\n")
    
    hat.dio_config_write_bit(channel3, DIOConfigItem.DIRECTION, 0)
    hat.dio_output_write_bit(channel3, DIO3)
    hat.dio_config_write_bit(channel7, DIOConfigItem.DIRECTION, 0)
    hat.dio_output_write_bit(channel7, DIO7)
    hat.a_out_write_all(values = val, options = options)
    
    if dolgo == 0:
        sleep(5)
        hat.dio_output_write_bit(channel3, 1)
        sleep(5)
        hat.dio_output_write_bit(channel7, 0)
        hat.a_out_write_all(values = [0, 0], options = options)
        hat.dio_reset()
    else:
        pass

# -----------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

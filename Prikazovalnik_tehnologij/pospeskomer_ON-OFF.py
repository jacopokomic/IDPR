from __future__ import print_function
from sys import version_info, stdout
from time import time, sleep
from daqhats import mcc172, OptionFlags, SourceType, HatIDs, HatError, AnalogInputMode, AnalogInputRange, DIOConfigItem
from daqhats_utils import select_hat_device
from daqhats_utils_128 import select_hat_device, enum_mask_to_string, chan_list_to_mask, input_mode_to_string, input_range_to_string

options_p = OptionFlags.CONTINUOUS
address_p = select_hat_device(HatIDs.MCC_172)
hat_p = mcc172(address_p)

scan_rate_p = 25600.0
    
channels = [0]
channel_mask = chan_list_to_mask(channels)
num_channels = len(channels)
samples_per_channel = 0

for channel in channels:
    state = hat_p.iepe_config_read(channel)
    
    if state == 0:
        hat_p.iepe_config_write(channel, 1)
        
        hat_p.a_in_clock_config_write(SourceType.LOCAL, scan_rate_p)
        
        synced = False
        while not synced:
            (_source_type, actual_scan_rate, synced) = hat_p.a_in_clock_config_read()
            if not synced:
                sleep(0.005)
    elif state == 1:
        hat_p.iepe_config_write(channel, 0)
    else:
        print("error")

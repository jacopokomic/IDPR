from __future__ import print_function
from sys import stdout, version_info
from time import time, sleep
from daqhats import mcc128, mcc152, mcc172, OptionFlags, SourceType, HatIDs, HatError, AnalogInputMode, AnalogInputRange, DIOConfigItem
from daqhats_utils import select_hat_device
from daqhats_utils_128 import select_hat_device, enum_mask_to_string, chan_list_to_mask, input_mode_to_string, input_range_to_string
from PyQt6 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import pyqtgraph as pg

READ_ALL_AVAILABLE = -1

options_m = OptionFlags.DEFAULT
address_m = select_hat_device(HatIDs.MCC_152)
hat_m = mcc152(address_m)
channel_m = 7

options_e = OptionFlags.CONTINUOUS
address_e = select_hat_device(HatIDs.MCC_128)
hat_e = mcc128(address_e)

options_p = OptionFlags.CONTINUOUS
address_p = select_hat_device(HatIDs.MCC_172)
hat_p = mcc172(address_p)

scan_rate_e = 100000.0
scan_rate_p = 25600.0
    
channels = [0]
channel_mask = chan_list_to_mask(channels)
num_channels = len(channels)
samples_per_channel = 0

hat_e.a_in_mode_write(AnalogInputMode.SE)
hat_e.a_in_range_write(AnalogInputRange.BIP_5V)

read_request_size = READ_ALL_AVAILABLE
timeout = 5.0

g = 9.81 # m/s^2
S = 0.1014 # V/g


class LastnaFrekvenca(pg.PlotWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.pospeskomer = Pospeskomer()
        
        self.curve = self.plot()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)
        
        self.a = []
        self.data = []
        self.ts = None
        self.tk = None
        self.n = False

    def update(self):
        read_result = hat_p.a_in_scan_read(read_request_size, timeout)
        samples_read = len(read_result.data)
        if samples_read > 0:
            self.data.extend(i/S for i in read_result.data)
            self.curve.setData(self.data)
            if min(self.data) > -1:
                del self.data[:samples_read]
            else:
                if len(self.a) > 400000:
                    self.tk = time()
                    self.timer.stop()
                    self.pospeskomer.stop()
                    self.n = True
                else:
                    if len(self.a) == 0:
                        self.ts = time()
                    else:
                        pass
                    self.a.extend(i/S for i in read_result.data)
        else:
            pass


class Pospeskomer:
	
    def __init__(self):
        hat_p.a_in_scan_start(channel_mask, samples_per_channel, options_p)

    def stop(self):
        hat_p.a_in_scan_stop()
        hat_p.a_in_scan_cleanup()


class Motor(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.miren()
        self.a = []
        self.ts = None
        self.tk = None
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        self.ax = self.figure.add_subplot(111)
        
        self.ax.set_xlabel("omega [rad/s]")
        self.ax.set_ylabel("X [mm]")
    
    def set_rpm(self, rpm):
        self.rpm = rpm
        self.DIO7, self.AO0x, self.AO1 = self.kanali(self.rpm)
        hat_m.dio_config_write_bit(channel_m, DIOConfigItem.DIRECTION, 0)
        hat_m.dio_output_write_bit(channel_m, self.DIO7)
        hat_m.a_out_write_all(values = [self.AO0x, self.AO1], options = options_m)
        sleep(1)
        self.dejrpm = self.get_rpm()
        self.AO0 = (self.rpm/self.dejrpm)*self.AO0x
        hat_m.a_out_write_all(values = [self.AO0, self.AO1], options = options_m)
    
    def get_rpm(self):
        hat_e.a_in_scan_start(channel_mask, 0, scan_rate_e, options_e)
        self.dejrpm = self.read_rpm(hat_e, num_channels)
        hat_e.a_in_scan_stop()
        hat_e.a_in_scan_cleanup()
        return self.dejrpm
    
    def read_rpm(self, hat, num_channels):
        total_samples_read = 0
        CH = []
        tm = 1
        tq = time() + tm
        while time() < tq:
            read_result = hat_e.a_in_scan_read(read_request_size, timeout)
            CH.extend(read_result.data)
        C = np.array(CH)
        count = np.sum(C[1:] > C[:-1] + 1.7)
        dejrpm = (count/1024)*(60/tm)
        return dejrpm
    
    def miren(self):
        hat_m.dio_config_write_bit(channel_m, DIOConfigItem.DIRECTION, 0)
        hat_m.dio_output_write_bit(channel_m, 0)
        hat_m.a_out_write_all(values = [0, 0], options = options_m)
        hat_m.dio_reset()

    def kanali(self, rpmfun):
        AO1 = 5.0
        if rpmfun < 0 or rpmfun > 3000:
            print("\n\tnapaka\n")
            exit()
        else:
            if rpmfun > 400:
                DIO7 = 1
                AO0x = (rpmfun/6000)*5
            else:
                DIO7 = 0
                AO0x = (rpmfun/400)*5
        return DIO7, AO0x, AO1
    
    def beri(self):
        p = []
        pt = []
        while len(pt) < 300000:
            read_result = hat_p.a_in_scan_read(read_request_size, timeout)
            samples_read = len(read_result.data)
            pt.extend(i/S for i in read_result.data)
            if len(pt) > 200000:
                if len(p) == 0:
                    t1 = time()
                else:
                    pass
                p.extend(i/S for i in read_result.data)
            else:
                pass
        t2 = time()
        self.a.extend(p)
        
        t = np.linspace(0, t2 - t1, len(p))
        dt = t[1] - t[0]
        accelerations = np.array(p)*g
        
        frequencies = fft.fftfreq(len(t), d = dt)
        accelerations_fft = fft.fft(accelerations)/len(t)

        half_n = len(t)//2
        single_sided_amplitude = 2*np.abs(accelerations_fft[:half_n])
        single_sided_amplitude[0] /= 2

        if len(t) % 2 == 0:
            single_sided_amplitude[-1] /= 2
        else:
            pass

        freq = frequencies[:half_n]
        
        ampmax = np.max(single_sided_amplitude*(freq < 30.0))
        am = np.argmax(single_sided_amplitude*(freq < 30.0))
        freqmax = freq[am]
        
        w = 2*np.pi*freqmax
        xmax = (ampmax/(w**2))*1000
        
        self.ax.plot(w, xmax, "o")
        
        self.canvas.draw()
    
    def prehod(self, lf, delta, rmin, rmax, korak):
        pospeskomer = Pospeskomer()
        r = rmin
        while r < rmax:
            self.set_rpm(r*lf)
            self.beri()
            self.miren()
            r += korak
        pospeskomer.stop()


class MotorWorker(QtCore.QThread):
    def __init__(self, motor, lf, delta):
        super().__init__()
        self.motor = motor
        self.lf = lf
        self.delta = delta

    def run(self):
        self.motor.prehod(lf = self.lf, delta = self.delta, rmin = 0.8, rmax = 1.4, korak = 0.02)


class Graf(QtWidgets.QWidget):

	def __init__(self, info, parent = None):
		super().__init__(parent)
        
		self.lfrpm = None
		self.delta = None
		self.a = info[0]
		self.ts = info[1]
		self.tk = info[2]
        
		self.figure = Figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)
        
		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.toolbar)
		layout.addWidget(self.canvas)
		self.setLayout(layout)
        
		self.prikazi()

	def prikazi(self):
		ax = self.figure.add_subplot(111)
		t = np.linspace(0, self.tk - self.ts, len(self.a))
		dt = t[1] - t[0]
		accelerations = np.array(self.a)*g
        
		tu = t[100000:]
		frequencies = fft.fftfreq(len(tu), d = dt)
		acc = accelerations[100000:]
		acc_fft = fft.fft(acc*np.hanning(len(tu)))
			
		ax.plot(tu, acc)
		ax.set_xlabel("t [s]")
		ax.set_ylabel("a [m/s^2]")
            
		ilf = np.argmax(acc_fft*(frequencies > 0))
		lf = frequencies[ilf]
		self.lfrpm = lf*60*2
		x1 = max(acc)
		x2 = max(acc*((tu >= 14.0) & (tu <= 15.0)))
		i1 = np.argwhere(acc == x1)
		i2 = np.argwhere(acc*((tu >= 14.0) & (tu <= 15.0)) == x2)
		st_nih = round((tu[i2[0][0]] - tu[i1[0][0]])*lf)
		self.delta = (np.log(x1/x2))/(2*np.pi*st_nih)
		
		self.canvas.draw()

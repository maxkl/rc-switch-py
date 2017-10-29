import os
from ctypes import cdll, c_void_p, c_char_p

lib = cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'librcswitch.so'))

lib.RCSwitch_RCSwitch.restype = c_void_p

lib.RCSwitch_switchOn.argtypes = [c_void_p, c_char_p, c_char_p]
lib.RCSwitch_switchOff.argtypes = [c_void_p, c_char_p, c_char_p]


class RCSwitch:
	@staticmethod
	def setup():
		lib.setup()

	def __init__(self):
		self.obj = lib.RCSwitch_RCSwitch()

	def set_pulse_length(self, pulse_length):
		lib.RCSwitch_setPulseLength(self.obj, pulse_length)

	def set_repeat_transmit(self, repeat_transmit):
		lib.RCSwitch_setRepeatTransmit(self.obj, repeat_transmit)
	
	def enable_transmit(self, pin):
		lib.RCSwitch_enableTransmit(self.obj, pin)

	def disable_transmit(self):
		lib.RCSwitch_disableTransmit(self.obj)

	def switch_on(self, group, device):
		lib.RCSwitch_switchOn(self.obj, group.encode('utf-8'), device.encode('utf-8'))

	def switch_off(self, group, device):
		lib.RCSwitch_switchOff(self.obj, group.encode('utf-8'), device.encode('utf-8'))

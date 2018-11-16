from resettabletimer import ResettableTimer
from time import sleep
import argparse

from pi_hcsr501 import HcSr501
from screen_utils import screen

class PiScreenOnOff(object):
	def __init__(self, timeout=15*60, pin=17):
		self.__sensor = HcSr501(pin)
		self.__timer = ResettableTimer(timeout, screen, [False])
		self.__timer.start()

	def __run(self):
		while True:
			if self.__sensor.active:
				screen(True)
				self.__timer.reset(start=True)
				sleep(0.5)

	def run(self):
		try:
			self.__run()
		except KeyboardInterrupt:
			self.__timer.cancel()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--pin", type=int, default=17, help="Pin used for PIR sensor connection")
	parser.add_argument("-t", "--timeout", type=int, default=5*60, help="Screen off timeout in seconds")
	args = parser.parse_args()

	print("Screen auto On-Off active")
	PiScreenOnOff(args.timeout, args.pin).run()
	print("\rScreen auto On-Off inactive")

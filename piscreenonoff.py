from resettabletimer import ResettableTimer
from time import sleep

from pi_hcsr501 import HcSr501
from screen_utils import screen

class PiScreenOnOff(object):
	def __init__(self, timeout=15*60):
		self.__sensor = HcSr501()
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
	print("Screen auto On-Off active")
	PiScreenOnOff(60).run()
	print("\rScreen auto On-Off inactive")

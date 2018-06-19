from time import sleep

import pigpio

class HcSr501(object):
	def __init__(self, pin=17):
		self.__pi = pigpio.pi()
		self.__pi.set_mode(17, pigpio.INPUT)

	@property
	def active(self):
		return bool(self.__pi.read(17))

if __name__ == "__main__":
	HCSR501 = HcSr501()

	while True:
		print(str(HCSR501.active) + " ", end="\r")
		sleep(0.5)

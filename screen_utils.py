import os

def screen(power_on):
	power = "1" if power_on else "0"
	os.system("vcgencmd display_power " + power)

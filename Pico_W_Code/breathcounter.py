from machine import Pin, ADC
from utime import sleep_ms

s = ADC(Pin(26))

def value():
	return int(s.read_u16() > 60_000)

def getReadings2():
	period = 5
	iterations = 0
	value()
	while value() == 0:
		sleep_ms(period)
	pressed = True
	counter = -1
	print("started")
	while counter < 6:
		if value() == 1:
			if not pressed:
				counter += 1
				print("pressed",counter, (period * iterations) // 1000)
				pressed = True
		else:
			pressed = False
		sleep_ms(period)
		iterations += 1
	return (counter * 60_000) / (period * iterations)

#while True:
#	sleep_ms(75)
#	print(s.read_u16())
from mymax import *
from machine import SoftI2C, Pin
from time import sleep_ms

sda = 4
scl = 5
freq = 400000

i2c = SoftI2C(sda=Pin(sda),scl=Pin(scl),freq=freq)

sensor = MyMax30102(i2c)
sleep_ms(500)

def getReadings():
	sensor.write(33,1)#turn on
	sleep_ms(500)
	roomTemp = int.from_bytes(sensor.read(20),"big") + int.from_bytes(sensor.read(21),"big")/16
	bpmList = []
	for i in range(100):
		rbuf = sensor.read(12,8)
		bpm = int.from_bytes(rbuf[2:6],"big")
		if bpm != 0:
			bpmList.append(bpm)
		sleep_ms(100)
	finalTemp = int.from_bytes(sensor.read(20),"big") + int.from_bytes(sensor.read(21),"big")/16
	if len(bpmList) != 0: #this is to avoid division by 0 errors
		aveBpm = sum(bpmList)/len(bpmList)
	else:
		aveBpm = 0
	sensor.write(33,2)#turn off
	return str(round(roomTemp))+","+str(round(finalTemp))+","+str(round(aveBpm))

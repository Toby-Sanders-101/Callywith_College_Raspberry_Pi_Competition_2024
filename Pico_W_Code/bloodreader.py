from Raspberry_Pi_Competition.mymax import *
from machine import SoftI2C, Pin
from utime import sleep_ms

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
	aveBpm = sum(bpmList)/len(bpmList)
	sensor.write(33,2)#turn off
	return str(round(roomTemp))+","+str(round(finalTemp))+","+str(round(aveBpm))

'''
while False:
	print(int.from_bytes(sensor.read(12,8)[2:6],"big"))
	sleep_ms(400)
while False:
	if True:
		rbuf = sensor.read(12,8)
		SPO2Valid = rbuf[1]
		HeartbeatValid = rbuf[7]
		SPO2 = rbuf[0]
		if SPO2 == 0:
			SPO2 = -1
		else:
			print("SPO2 is : "+str(SPO2)+"%")
		heartbeat = int(rbuf[2]) << 24 | int(rbuf[3]) << 16 | int(rbuf[4]) << 8 | int(rbuf[5])
		if heartbeat == 0:
			heartbeat = -1
		else:
			print("heart rate is : "+str(heartbeat)+"bpm")
		#b = int.from_bytes(sensor.read(20),"big") + int.from_bytes(sensor.read(21),"big")/16
		#if b!=0:
			#print("temperature is :",b)
	sleep_ms(100)
'''

import socket
import time
import network
from machine import *
import bloodreader as bloodreader
import breathcounter as breathcounter

Pin(2,Pin.OUT).value(0)
Pin(1,Pin.OUT).value(1)
time.sleep_ms(2000)
Pin(1,Pin.OUT).value(0)

def getonlan():
	ssid = "HUAWEI-0411DD" #change this to the name of your WiFi
	password = "password" # and the password of it
	
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.connect(ssid, password)
	
	max_wait = 10
	while max_wait > 0:
		if wlan.status() < 0 or wlan.status() >= 3:
			break
		max_wait -= 1
		time.sleep(1)
	
	if wlan.status() != 3:
		print('network connection failed')
		return False
	else:
		print(wlan.status())
		print(wlan.ifconfig())
		return True

def setupsocket():
	try:
		addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
		s = socket.socket()
		s.bind(addr)
		s.listen(10)
		print('listening on', addr)
		return s, addr
	except:
		print("error, you may want to reset(). make sure you run from main.py")
		return "error", "error"

class Client():
	def __init__(self, s):
		self.s = s
		cl, addr = s.accept()
		print('client connected from', addr)
		self.cl = cl
		self.addr = addr
		self.count = 0

	def getblood(self):
		print("\nSending to",self.addr,":\t","On it!")
		self.cl.send("On it!")
		print("Sent")
		return bloodreader.getReadings()

	def getair(self):
		print("\nSending to",self.addr,":\t","On it!")
		self.cl.send("On it!")
		print("Sent")
		return str(round(breathcounter.getReadings2()))

	def getmsg(self):
		request = str(self.cl.recv(1024).decode('ASCII'))
		print("\nReceived from",self.addr,":\t",request)
		return request

	def respondTo(self, request):
		if request in ["Establishing connection","end"]:
			response = request
		elif request=="blood":
			response = self.getblood()
		elif request=="air":
			response = self.getair()
		else:
			response = "Umm, I don't know what to say to that"
		
		print("\nSending to",self.addr,":\t",response)
		try:
			self.cl.send(str(response))
			print("Sent")
		except:
			print("Failed to send (socket is probably closed)")
			return False
		
		return request!="end"

	def close(self):
		self.cl.close()

onlan = getonlan()
for i in range(10):
	if not onlan:
		print("failed\n")
		time.sleep_ms(500)
		print("attempt "+str(i+2)+"...")
		Pin(2,Pin.OUT).value(1)
		time.sleep_ms(500)
		Pin(2,Pin.OUT).value(0)
		onlan = getonlan()
if onlan:
	print("succeeded")
	Pin(2,Pin.OUT).value(1)
	s, myAddr = setupsocket()
	if myAddr!="error":
		while True:
			print("Waiting for client...")
			client = Client(s)
			continueTalking = True
			while continueTalking:
				request = client.getmsg()
				continueTalking = client.respondTo(request)
				client.count += 1
			client.close()

Pin(1,Pin.OUT).value(1)
time.sleep_ms(2000)
Pin(1,Pin.OUT).value(0)

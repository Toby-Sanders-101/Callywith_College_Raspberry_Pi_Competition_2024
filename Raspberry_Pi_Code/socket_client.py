import socket
import time
import func_timeout

class Connection:
	def __init__(self, gui):
		self.gui = gui
		self.running = False
		pico = socket.getaddrinfo("10.0.0.20",80)
		print(pico)
		s = socket.socket()
		s.connect(pico[0][-1])
		self.s = s
	
	def send(self,msg):
		self.s.send(bytes(msg,'utf-8'))
		print(msg,"sent")
	
	def getblooddata(self):
		if not self.running:
			return False
		self.send("blood")
		try:
			recv = func_timeout.func_timeout(5, self.receive)
		except func_timeout.FunctionTimedOut as e:
				print(e)
				return False
		if recv=="On it!":
			try:
				recv2 = func_timeout.func_timeout(40, self.receive).split(",")
			except func_timeout.FunctionTimedOut as e:
				print(e)
				return False
			self.gui.update_all_data("roomTemp", int(recv2[0]))
			self.gui.update_all_data("bodyTemp", int(recv2[1]))
			self.gui.update_all_data("bpm", int(recv2[2]))
			self.gui.update_lbl(3,2,"Room temperature:\t\t"+str(int(recv2[0]))+"'C")
			self.gui.update_lbl(3,3,"Body temperature:\t\t"+str(int(recv2[1]))+"'C")
			self.gui.update_lbl(3,4,"Heart rate (bpm):\t\t"+str(int(recv2[2])))
			return True
			
	def getairdata(self):
		if not self.running:
			return False
		self.send("air")
		try:
			recv = func_timeout.func_timeout(5, self.receive)
		except func_timeout.FunctionTimedOut as e:
				print(e)
				return False
		if recv=="On it!":
			recv2 = self.receive()
			self.gui.update_all_data("breathrate",int(recv2))
			self.gui.update_lbl(4,2,"Breathing rate (bpm):\t\t"+recv2)
			return True
	
	def receive(self):
		recv = self.s.recv(1024).decode('ASCII')
		recv = str(recv)
		print(recv,"received")
		if recv=="end":
			self.s.close()
			print("Socket closed")
			self.running = False
		return recv

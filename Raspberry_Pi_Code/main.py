import time
import threading
from gui import GUI
from socket_client import Connection
from harry import Harry
gui = None
waiting = True

def make_gui():
	global gui
	gui = GUI()
	gui.start()
	gui.endconnection()
	quit()

gui_thread = threading.Thread(target=make_gui)
gui_thread.start()

while waiting:
	if gui != None:
		waiting = gui.waiting
	time.sleep(0.1)

def train_harry():
	bot = Harry()
	gui.bot = bot

harry_trainer_thread = threading.Thread(target=train_harry)
harry_trainer_thread.start()

conn = None
def startconn():
	global conn, gui
	try:
		conn = Connection(gui)
		gui.conn = conn
		conn.send("Establishing connection")
		if conn.receive() == "Establishing connection":
			conn.running = True
	except:
		time.sleep(1)
		startconn()

startconn()

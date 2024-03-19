from tkinter import *
from tkinter import ttk, messagebox

all_data = {}
for key in ["name","sex","age","weight","height","roomTemp","bodyTemp","bpm","waist","exercise","alcohol","water","breathrate"]:
	all_data[key] = None
all_data = {"name":"toby","sex":"m","age":17,"weight":68,"height":180,"roomTemp":20,"bodyTemp":37,"bpm":80,"waist":82,"exercise":180,"alcohol":3.5,"water":2.3,"breathrate":15}

class MyEntry(Entry):
	
	#entry for strings
	def validateStr(self, value):
		if value=="":
			try:
				all_data[self.key] = None
			except:
				pass
			return True
		if len(value)>20:
			return False
		try:
			all_data[self.key] = str(value)
		except:
			pass
		finally:
			return True
	
	def makeStr(self, key):
		self.key = key
		vcmd = (self.register(self.validateStr), '%P')
		self.config(validate="all", validatecommand=vcmd)
	
	#entry for integers
	def validateInt(self, value):
		if value=="":
			try:
				all_data[self.key] = None
			except:
				pass
			return True
		if len(value)>3:
			return False
		flag = True
		for char in value:
			if not char in ["1","2","3","4","5","6","7","8","9","0"]:
				flag = False
		if flag:
			try:
				all_data[self.key] = int(value)
			except:
				pass
		return flag
	
	def makeInt(self, key):
		self.key = key
		vcmd = (self.register(self.validateInt), '%P')
		self.config(validate="all", validatecommand=vcmd)
	
	#entry for floats
	def validateFloat(self, value):
		if value=="":
			try:
				all_data[self.key] = None
			except:
				pass
			return True
		if len(value)>4 or value.count(".")>1:
			return False
		flag = True
		for char in value:
			if not char in ["1","2","3","4","5","6","7","8","9","0","."]:
				flag = False
		if flag:
			try:
				all_data[self.key] = float(value)
			except:
				pass
		return flag
	
	def makeFloat(self, key):
		self.key = key
		vcmd = (self.register(self.validateFloat), '%P')
		self.config(validate="all", validatecommand=vcmd)
		

class GUI:
	def __init__(self):
		self.w = 1050
		self.h = 500
		
		self.conn = None
		self.bot = None
		self.waiting = True
		
		root = Tk()
		root.title("Health display")
		root.geometry(str(self.w)+"x"+str(self.h))
		root.resizable(0,0)
		self.root = root
		boxes = ["Basic","Measurements","Lifestyle","Blood/Temperature","Breathing","Finish"]
		frames = []
		for i in range(len(boxes)):
			frames.append(self.make_box(boxes[i],i))
		self.basicfr(frames[0])
		self.measurefr(frames[1])
		self.lifestylefr(frames[2])
		self.bloodfr(frames[3])
		self.airfr(frames[4])
		self.finishfr(frames[5])
		
		root.bind('<Return>', self.go_to_next_entry)
			
	def start(self):
		self.waiting = False
		self.root.mainloop()
	
	def msg(self, title, text):
		messagebox.showerror(title, text)
	
	@staticmethod
	def all_children(wid):
		_list = wid.winfo_children()
		for item in _list:
			if item.winfo_children():
				_list.extend(item.winfo_children())
		return _list
	
	def update_all_data(self, key, value):
		all_data[key] = value
	
	def update_lbl(self, frame_num, lbl_num, text):
		frame = GUI.all_children(self.root)[frame_num]
		label = GUI.all_children(frame)[lbl_num]
		label.config(text=text)
	
	def go_to_next_entry(self, event):
		current = self.root.focus_get()
		widgets = GUI.all_children(self.root)
		i = widgets.index(current)
		nextWidget = Label()
		j = 0
		while type(nextWidget) in [type(Label()),type(Frame())]:
			j += 1
			nextWidget = widgets[(i+j)%len(widgets)]
		nextWidget.focus_set()
	
	def make_box(self, title, pos):
		frame = Frame(self.root, bg='white', bd=4, relief=SOLID)
		label = Label(frame, text=title, bg='red')
		label.place(relx=0.5,y=10,height=20,anchor=CENTER)
		frame.place(x=(self.w/3)*(pos%3),y=(self.h/2)*(pos//3),width=(self.w/3),height=(self.h/2))
		return frame
	
	def basicfr(self, fr):
		lbl1 = Label(fr, text="Name:")
		lbl1.place(x=10, y=30)
		ent1 = MyEntry(fr)
		ent1.makeStr("name")
		ent1.place(x=10, y=50)
		ent1.focus_set()
		lbl2 = Label(fr, text="Biological sex:")
		lbl2.place(x=10, y=80)
		self.sex = StringVar()
		rad1 = Radiobutton(fr, text="Female", variable=self.sex, value="f")
		rad1.place(x=10, y=100)
		rad2 = Radiobutton(fr, text="Male", variable=self.sex, value="m")
		rad2.place(x=120, y=100)
		lbl3 = Label(fr, text="Age:")
		lbl3.place(x=10, y=130)
		num1 = MyEntry(fr)
		num1.makeInt("age")
		num1.place(x=10, y=150)
	
	def measurefr(self, fr):
		lbl1 = Label(fr, text="Weight (kg):")
		lbl1.place(x=10, y=30)
		num1 = MyEntry(fr)
		num1.makeInt("weight")
		num1.place(x=10, y=50)
		lbl2 = Label(fr, text="Height (cm):")
		lbl2.place(x=10, y=80)
		num2 = MyEntry(fr)
		num2.makeInt("height")
		num2.place(x=10, y=100)
		lbl3 = Label(fr, text="Waist size (cm):")
		lbl3.place(x=10, y=130)
		num3 = MyEntry(fr)
		num3.makeInt("waist")
		num3.place(x=10, y=150)
	
	def lifestylefr(self, fr):
		lbl1 = Label(fr, text="Moderately intense exercise per week (mins):")
		lbl1.place(x=10, y=30)
		num1 = MyEntry(fr)
		num1.makeInt("exercise")
		num1.place(x=10, y=50)
		lbl2 = Label(fr, text="Units of alcohol per week:")
		lbl2.place(x=10, y=80)
		num2 = MyEntry(fr)
		num2.makeInt("alcohol")
		num2.place(x=10, y=100)
		lbl3 = Label(fr, text="Water drank daily (litres):")
		lbl3.place(x=10, y=130)
		num3 = MyEntry(fr)
		num3.makeFloat("water")
		num3.place(x=10, y=150)
	
	def changestateto(self, state):
		for child in GUI.all_children(self.root):
			try:
				child["state"] = state
			except:
				pass
	
	def getblood(self):
		messagebox.showinfo("Instructions", "Place your finger on the sensor")
		self.changestateto(DISABLED)
		self.root.update()
		if self.conn is not None:
			if self.conn.running:
				if self.conn.getblooddata():
					self.root.update()
					self.changestateto(NORMAL)
					return True
		self.msg("Connectivity error", "Please connect to a pico")
		self.changestateto(NORMAL)
	
	def bloodfr(self, fr):
		btn1 = Button(fr, text="Get readings", command=self.getblood)
		btn1.place(x=10, y=30)
		lbl1 = Label(fr, text="Room temperature:\t\t---")
		lbl1.place(x=10,y=70)
		lbl2 = Label(fr, text="Body temperature:\t\t---")
		lbl2.place(x=10,y=90)
		lbl3 = Label(fr, text="Heart rate (bpm):\t\t---")
		lbl3.place(x=10,y=110)
	
	def getanswer(self):
		self.changestateto(DISABLED)
		self.root.update()
		if self.bot is not None:
			question = self.questionentry.get()
			answer = self.bot.getanswer(question)
			self.answerlbl.config(text=answer)
		else:
			self.answerlbl.config(text="Harry is unavailable at this time :(")
		self.changestateto(NORMAL)
	
	def loadharryfr(self):
		for child in self.root.winfo_children():
			child.destroy()
			
		self.root.title = "Harry the Health Expert"
		
		lbl1 = Label(self.root, text="Ask Harry the Health Expert...", font=("Arial", 16))
		lbl1.place(relx=0.5, rely=0.2,anchor=CENTER)
		ent1 = Entry(self.root, font=("Arial", 16))
		ent1.place(relx=0.5, rely=0.3,anchor=CENTER)
		btn1 = Button(self.root, text="Get answer", font=("Arial", 16), command=self.getanswer)
		btn1.place(relx=0.4, rely=0.4,anchor=CENTER)
		btn2 = Button(self.root, text="Quit", font=("Arial", 16), command=self.root.destroy)
		btn2.place(relx=0.6,rely=0.4,anchor=CENTER)
		lbl2 = Label(self.root, font=("Arial",16), wraplength = 700, justify=CENTER)
		lbl2.place(relx=0.5,rely=0.7,anchor=CENTER)
		
		self.questionentry = ent1
		self.answerlbl = lbl2
	
	def resultsfr(self, fr):
		lbl1 = Label(fr, font=("Arial", 14))
		lbl1.place(relx=0.5,rely=0.4,width=self.w * 0.9,anchor=CENTER)
		btn1 = Button(fr, text="Ask Harry...", font=("Arial", 16), command=self.loadharryfr)
		btn1.place(relx=0.3,rely=0.9,anchor=CENTER)
		btn2 = Button(fr, text="Quit", font=("Arial", 16), command=self.root.destroy)
		btn2.place(relx=0.6,rely=0.9,anchor=CENTER)
	
	def getair(self):
		messagebox.showinfo("Instructions", "Once you've closed this box, start pressing the button on the device at the peak of each breath and continue until done")
		self.changestateto(DISABLED)
		self.root.update()
		if self.conn is not None:
			if self.conn.running:
				if self.conn.getairdata():
					self.root.update()
					self.changestateto(NORMAL)
					return True
		self.msg("Connectivity error", "Please connect to a pico")
		self.changestateto(NORMAL)
	
	def airfr(self, fr):
		btn1 = Button(fr, text="Get readings", command=self.getair)
		btn1.place(x=10, y=30)
		lbl1 = Label(fr, text="Breathing rate (bpm):\t\t---")
		lbl1.place(x=10,y=70)
	
	def submit(self):
		if self.sex.get() in ["m","f"]:
			all_data["sex"] = self.sex.get()
		flag = True
		for key, value in all_data.items():
			if value is None:
				flag = False
		print(all_data)
		if not flag:
			self.msg("Incomplete sections", "Please complete every box")
		else:
			self.endconnection()
			
			for child in self.root.winfo_children():
				child.destroy()
			
			self.root.title = "Results"
			self.resultsfr(self.root)
			self.root.configure(background='white')
			
			bmi = 10_000 * all_data["weight"]/(all_data["height"] ** 2)
			if bmi < 18.5:
				bmiCat = "Underweight"
				count = 1
			elif bmi < 25:
				bmiCat = "Healthy"
				count = 0
			elif bmi < 30:
				bmiCat = "Overweight"
				count = 1
			elif bmi < 40:
				bmiCat = "Obese"
				count = 2
			else:
				bmiCat = "Severely Obese"
				count = 3
			
			tooMuchAlcohol = all_data["alcohol"] > 14
			notEnoughExercise = all_data["exercise"] < 150
			notEnoughWater = all_data["water"] < 2
			lowHeartRate = (all_data["bpm"] < 60) and (notEnoughExercise or bmi >= 25)
			highHeartRate = all_data["bpm"] > 120
			lowBreathRate = all_data["breathrate"] < 12
			highBreathRate = all_data["breathrate"] > 20
			coldRoom = all_data["roomTemp"] < 17
			hotRoom = all_data["roomTemp"] > 22
			coldBody = all_data["bodyTemp"] < 35
			hotBody = all_data["bodyTemp"] > 37.5
			if all_data["sex"] == "m":
				tooWide = all_data["waist"] > 94
			else:
				tooWide = all_data["waist"] > 80
				
			arr = [tooMuchAlcohol, notEnoughExercise, notEnoughWater, lowHeartRate, highHeartRate,
				lowBreathRate, highBreathRate, coldRoom, hotRoom, coldBody, hotBody, tooWide]
			
			suggestions = ["Aim to reduce your alcohol intake and spread them across the week",
				"Try to set aside a few hours a week for high-intensity exercise",
				"Make sure you drink at least 2 litres of water/fluids a day (ideally 2.5l)",
				"You have a low heart rate which could be a sign of bradycardia. You may want to get this checked out",
				"You have a high heart rate which could be a sign of tachycardia. You may want to get this checked out",
				"You have a low breathing rate which could be a sign of bradypnea. You may want to get this checked out",
				"You have a high breathing rate which could be a sign of tachypnea. You may want to get this checked out",
				"Your room is quite cold, you may want to put the heating on",
				"Your room is quite hot, you may want to open the windows",
				"Your body temperature is quite low, you should put some more layers on to warm yourself up",
				"Your temperature is quite high, you should have a cold drink to cool yourself down",
				"Aim to reduce your calorie intake or increase the amount of energy you burn"]
			
			for attr in arr:
				if attr is True:
					count += 1
			
			label = GUI.all_children(self.root)[0]
			
			if count == 0:
				overall = "You seem perfectly healthy - keep up the good work!"
				label.configure(background='green')
			elif count < 4:
				overall = "You're very healthy but there a few things you could tweak..."
				label.configure(background='green')
			elif count < 7:
				overall = "Seems like you need  bit of refresher on how to stay healthy. Here are a few tips:"
				label.configure(background='orange')
			else:
				overall = "Looks like you really aren't taking good care of yourself. Take note of these potential improvements:"
				label.configure(background='red')
			
			text = "The results are in...\n\n"+overall+"\n"
			for i in range(12):
				if arr[i] is True:
					text = text + "\n - " + suggestions[i]
			text = text + "\n\nBased on your BMI, you are: " + bmiCat
			label.config(text=text)
			
	
	def endconnection(self):
		if self.conn is not None:
			if self.conn.running:
				self.conn.running = False
				self.conn.send("end")
	
	def finishfr(self, fr):
		btn1 = Button(fr, text="Submit", command=self.submit)
		btn1.place(x=10, y=30)
		btn2 = Button(fr, text="End connection", command=self.endconnection)
		btn2.place(x=10, y=70)

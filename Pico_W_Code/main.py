import Raspberry_Pi_Competition.compmain
'''
from mymax import *
from machine import SoftI2C, Pin
from utime import sleep_ms
import random

red = 33
sda = 16
scl = 17
freq = 400000

i2c = SoftI2C(sda=Pin(sda),scl=Pin(scl),freq=freq)

sensor = MyMax30102(i2c)
sensor.readall()
#for i in [4,6,7,8]:
#    sensor.write(i,64)
#for i in range(11,40):
#    sensor.write(i,64)
sleep_ms(1000)
sensor.readall()

#import find_ap
#import baro

#from ap_maker import *
#from machine import Pin
#import random
#import wireless

print("hello from main.py")

ssid = "Pico"
ap = create_ap(ssid,"password")
get_ap_info(ap)
s = create_socket("0.0.0.0",80)
print(s)
if type(s)!=type(1):
    inp = "y"
    while "y" in inp:
        inp = "y"#input("Open/re-open socket?")
        if not "y" in inp:
            break;
        response = "blank"
        conn, addr = get_client(s)
        Pin(16, Pin.OUT).value(1)
        while response!="":
            response = "hello world!"#input("Response: ")
            send(conn, response)
            print(conn.recv(1024))
        print("Closing conn:",conn)
        conn.close()
        Pin(16, Pin.OUT).value(0)
    s.close()
'''
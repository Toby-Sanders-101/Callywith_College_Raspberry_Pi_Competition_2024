from machine import SoftI2C

addr = 0x57

class MyMax30102:
    def __init__(self, _i2c):
        self.i2c = _i2c
    
    def write(self, reg, val):
        self.i2c.writeto_mem(addr, reg, bytes([val]))
    
    def read(self, reg, n_bytes=1):
        self.i2c.writeto(addr, bytearray([reg]))
        return self.i2c.readfrom(addr, n_bytes)
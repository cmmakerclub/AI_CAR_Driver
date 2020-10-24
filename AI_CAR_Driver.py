import time
import struct

class CAR_Driver:
    def __init__(self, i2c, address=0x12):
        self.i2c = i2c
        self.address = address

    def buzzer(self,timelong = 0):  #ฟังชั้นเปิดเสียง ตัวเลข 1 = 50mS  หรือ 2 = 100mS
        if timelong >= 255 :
            timelong = 255
        a = self.i2c.writeto(self.address,bytes([int(timelong)]))
        return a

    def servomotor(self,M2=0,M3=0,M4=0):  # ฟังชั้นขับโซโวมอเตอร์  มี 4 ช่อง M1,M2,M3,M4 ค่า 0-255 map 1000-2000 uS
        if M2 >= 255 :
            M2 = 255
        if M3 >= 255 :
            M3 = 255
        if M4 >= 255 :
            M4 = 255
        a = self.i2c.writeto(self.address,bytes([int(0),int(M2),int(M3),int(M4)]))
        return a
    def carmotor(self,FB = 128,LR = 128):  # ฟังชั้น FB คือ เดินหน้า ถอยหลัง   LR คือ  เลี้ยวซ้าย ขวา
    #     if FB >= 255 :
    #         FB = 255
    #     if LR >= 255 :
    #         LR = 255

        a = self.i2c.writeto(self.address,bytes([int(FB),int(LR),int(0)]))
        return a
    def setname_bl(self,_num = 0):  # ฟังชั้นเปลียนซื่อ Blใส่ได้แต่ตัวเลขเท่านั้น
    #     if _num >= ุ60000 :
    #         _num = 60000
        _namenum = struct.pack(">H", _num)
        a = self.i2c.writeto(self.address,_namenum)
        print(_namenum)
        return a
    def resdData(self):
        a = self.i2c.readfrom(self.address, 3)
        return a
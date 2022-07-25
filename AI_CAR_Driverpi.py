import smbus
import struct
import math

class CAR_Driver():

    DEVICE_ADDRESS = 0x12
    bus_device = smbus.SMBus(1) 
#     def value_limit(self, _value=0.0, min=-30000.0, max=30000.0):
#         if _value < min :
#             _value = min
#         if _value > max :
#             _value = max
#         return float(_value)

#     def Set_motorxyz(self, _valuex = 0.0, _valuey = 0.0, _valuez = 0.0):
#         _valuex = self.value_limit(_valuex, min=-1.0, max=1.0)
#         _valuey = self.value_limit(_valuey, min=-1.0, max=1.0)
#         _valuez = self.value_limit(_valuez, min=-1.0, max=1.0)
#         datas1 = struct.pack('>B', int(2))
#         datas2 = struct.pack('fff', float(_valuex), float(_valuey), float(_valuez))
#         self.bus_device.write(datas1+datas2)

    def buzzer(self,timelong = 0):  #ฟังชั้นเปิดเสียง ตัวเลข 1 = 50mS  หรือ 2 = 100mS
        if timelong >= 255 :
            timelong = 255
        a = self.bus_device.write_byte(self.DEVICE_ADDRESS,timelong)
        return a

    def servomotor(self,M2=0,M3=0,M4=0):  # ฟังชั้นขับโซโวมอเตอร์  มี 4 ช่อง M1,M2,M3,M4 ค่า 0-255 map 1000-2000 uS
        if M2 >= 255 :
            M2 = 255
        if M3 >= 255 :
            M3 = 255
        if M4 >= 255 :
            M4 = 255
        a = self.bus_device.write_i2c_block_data(self.DEVICE_ADDRESS,int(0),[int(M2),int(M3),int(M4)])
        return a
    def carmotor(self,FB = 128,LR = 128):  # ฟังชั้น FB คือ เดินหน้า ถอยหลัง   LR คือ  เลี้ยวซ้าย ขวา
    #     if FB >= 255 :
    #         FB = 255
    #     if LR >= 255 :
    #         LR = 255

        a = self.bus_device.write_i2c_block_data(self.DEVICE_ADDRESS,int(FB),[int(LR),int(0)])
        return a
    def setname_bl(self,_num = 0):  # ฟังชั้นเปลียนซื่อ Blใส่ได้แต่ตัวเลขเท่านั้น
    #     if _num >= ุ60000 :
    #         _num = 60000
        _namenum = list(struct.pack(">H", _num))
        a = self.bus_device.write_i2c_block_data(self.DEVICE_ADDRESS,_namenum[0],_namenum[1])
        print(_namenum)
        return a
    def resdData(self):
        result = self.bus_device.read_i2c_block_data(self.DEVICE_ADDRESS, 0, 3)
        return result

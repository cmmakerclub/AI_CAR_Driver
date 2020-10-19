import sensor, image, time ,lcd
import KPU as kpu
from fpioa_manager import fm
from machine import I2C
from board import board_info
from Maix import GPIO
import struct
i2c = I2C(I2C.I2C0, freq=100000, scl=35, sda=34)

#///////////////////////////////////////////////////////// สำหรับ AI CAR V2 , AI CAR Driver
def buzzer(timelong = 0):  #ฟังชั้นเปิดเสียง ตัวเลข 1 = 50mS  หรือ 2 = 100mS
    if timelong >= 255 :
        timelong = 255
    a = i2c.writeto(0x12,bytes([int(timelong)]))
    return a

def servomotor(M2=0,M3=0,M4=0):  # ฟังชั้นขับโซโวมอเตอร์  มี 4 ช่อง M1,M2,M3,M4 ค่า 0-255 map 1000-2000 uS
    if M2 >= 255 :
        M2 = 255
    if M3 >= 255 :
        M3 = 255
    if M4 >= 255 :
        M4 = 255
    a = i2c.writeto(0x12,bytes([int(0),int(M2),int(M3),int(M4)]))
    return a
def carmotor(FB = 128,LR = 128):  # ฟังชั้น FB คือ เดินหน้า ถอยหลัง   LR คือ  เลี้ยวซ้าย ขวา
#     if FB >= 255 :
#         FB = 255
#     if LR >= 255 :
#         LR = 255

    a = i2c.writeto(0x12,bytes([int(FB),int(LR),int(0)]))
    return a
def setname_bl(_num = 0):  # ฟังชั้นเปลียนซื่อ Blใส่ได้แต่ตัวเลขเท่านั้น
#     if _num >= ุ60000 :
#         _num = 60000
    _namenum = struct.pack(">H", _num)
    a = i2c.writeto(0x12,_namenum)
    print(_namenum)
    return a
#///////////////////////////////////////////////////////////////////
sensor.reset(freq=24000000,dual_buff=True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)
sensor.set_vflip(1)
sensor.run(1)

clock = time.clock()
toss1 = 0

lcd.init()

task = kpu.load(0x600000)

#task = kpu.load("/sd/t6.kmodel")
##datazzz = bytes([int(128),int(128),int(0)])
a = kpu.set_outputs(task,0,1,1,1)
try:
    while(True):
        toss = toss1
        toss1 = time.ticks_ms()
        #print(1000/(toss1-toss))
        #img = image.Image("/sd/dataset/55.jpg")
        img = sensor.snapshot()
        #img = img.draw_rectangle(0,0,320,80,color=(0,0,0),fill=True)
        ##img = img.draw_rectangle(130,180,90,240-180,color=(0,0,0),fill=True)
        img = img.resize(160,160)

        ##img = img.draw_rectangle(0,180,224,320,color=(0,0,0),fill=True)
        a = img.pix_to_ai()
        #print(img[0])

        fmap = kpu.forward(task,img)
        plist=fmap[:]
        #pmax=max(plist)
        #max_index=plist.index(pmax)
        #print(plist)
        txx = 0
        if abs(plist[0]) >0.1 :
            txx = (plist[0])*128

        #print(txx)
        ##txx = txx*1.5
        if txx > 127 :
            txx = 127
        if txx < -127 :
            txx = -127
        #print(txx)
        #datazzz = bytes([int(128),int(txx+127),int(0)])
        ####print(datazzz)
        #a = i2c.writeto(0x12,bytes([int(165),int(txx+127),int(0)]))
        a = carmotor(int(165),int(txx+127),int(0))
        #lcd.display(img)
        #lcd.draw_string(90, 0, str(int(1000/(toss1-toss)))+" fps", lcd.RED,lcd.BLACK)
        #lcd.display(img2)

except KeyboardInterrupt :
    a = kpu.deinit(task)
# AI_CAR_Driver
<!-- Copy and paste the converted output. -->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 6.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**คู่มือการใช้งาน บอร์ด AI CAR Driver**

	บอร์ด AI CAR Driver เป็นเบอร์ดที่ช่วยในการขับมอเตอร์ ในบอร์ดมี HM-10 เป็นบลูทูธ 4.0 ที่เอาใวรับข้อมูลจาก APP Remote xy ที่ช่วยในการบังคับรถ แล้วสามารถดึงข้อมูลการบังคับรถระหว่างบังคับได้ มีระบบเตือนเวลาแบตเตอรี่ต่ำ บอร์ดรองรับไฟได้ 2s 3s 4s เป็นแบตเตอรี่ ชนิด lipo สามารถสั่งให้ SERVO หมุนได้อีก 3 ช่อง

PINOut 



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")




<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")




<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


จุดต่อมอเตอร์หลัง แบบ DC Motor



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


จุดต่อมอเตอร์ Servo 



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


def buzzer(timelong = 0):  #ฟังชั้นเปิดเสียง ตัวเลข 1 = 50mS  หรือ 2 = 100mS

    if timelong >= 255 :

        timelong = 255

    a = i2c.writeto(0x12,bytes([int(timelong)]))

    return a

def servomotor(M1 = 0,M2=0,M3=0,M4=0):  # ฟังชั้นขับโซโวมอเตอร์  มี 4 ช่อง M1,M2,M3,M4 ค่า 0-255 map 1000-2000 uS

    if M1 >= 255 :

        M1 = 255

    if M2 >= 255 :

        M2 = 255

    if M3 >= 255 :

        M3 = 255

    if M4 >= 255 :

        M4 = 255

    a = i2c.writeto(0x12,bytes([int(M1),int(M2),int(M3),int(M4)]))

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

การใช้งาน



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")

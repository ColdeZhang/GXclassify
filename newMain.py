# change ACM number as found from ls /dev/tty/ACM*
import UIExecutor as UI
import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600

browser = UI.init()
read_ser = ""
#----------可回收物---厨余垃圾---其他垃圾---有害垃圾
#----------容量-个数--容量-个数--容量-个数--容量-个数
devInfo = [  0,  0,   0,  0,   0,  0,   0,  0]
US = [4,17,27,22,5,6,13,19]
#---------五号电池；橘子皮；不规则水泥块；废报纸团；易拉罐；矿泉水瓶
nameNum = [0,     0,     0,          0,      0,     0]

for i in range(4):
    GPIO.setup(US[i*2], GPIO.OUT)
    GPIO.setup(US[i*2+1], GPIO.IN)


while True:
    read_ser = ser.readline()
    print(read_ser)
    if(read_ser == "playvideo"):
        UI.videoPage(browser)
        read_ser = ""
        pass
    elif(read_ser == "youhailaji"):
        UI.waitingPage(browser, '这是有害垃圾')
        devInfo[7] = devInfo[7]+1
        read_ser = ""
        pass
    elif(read_ser == "qitalaji"):
        UI.waitingPage(browser, '这是其他垃圾')
        devInfo[5] = devInfo[5]+1
        read_ser = ""
        pass
    elif(read_ser == "kehuishouwu"):
        UI.waitingPage(browser, '这是可回收物')
        devInfo[1] = devInfo[1]+1
        read_ser = ""
        pass
    elif(read_ser == "chuyulaji"):
        UI.waitingPage(browser, '这是厨余垃圾')
        devInfo[3] = devInfo[3]+1
        read_ser = ""
        pass
    elif(int(read_ser)>0 and int(read_ser)<7):
        nameNum[int(read_ser)-1] = nameNum[int(read_ser)-1] + 1
        read_ser = ""
        pass
    elif(read_ser == "end"):
        UI.listPage(browser, nameNum)
        read_ser = ""
    elif(read_ser == "manzaijiance"):
        UI.waitingPage(browser, '检测容量中……')
        for i in range(4):
            GPIO.output(US[i*2], GPIO.HIGH)
            time.sleep(0.00015)
            GPIO.output(US[i*2], GPIO.LOW)
            while not GPIO.input(US[i*2+1]):
                pass
            t1 = time.time()
            while GPIO.input(US[i*2+1]):
                pass
            t2 = time.time()
            dis = (t2 - t1) * 340 * 1000 / 2
            res = 300 - dis
            if res < 0:
                res = 0
            else:
                pass
            devInfo[i*2] = round((res/300)*100, 1)
        read_ser = ""
        pass
    elif(read_ser == "fenleiwancheng"):
        UI.devInfoPage(browser, devInfo)
        read_ser = ""
        pass

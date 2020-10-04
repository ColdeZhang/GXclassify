import objectRecogni
import RPi.GPIO as GPIO
import sys
import time
import UIExecutor as UI


btnPin = 4
usPin = 17
usEcho = 18
obsSen = 27
#--------------1-----2-----3
#-------------压缩---旋转---投放
#------------s--r--s---r--s--r
stepperPin = [5, 6, 13, 19, 26, 25]
lmtSwitch = [24, 22, 23]

devPos = 0
browser = UI.init()

def devInit():
    '设备初始化'
    UI.waitingPage(browser, '设备启动初始化中……')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(usPin, GPIO.OUT)
    GPIO.setup(usEcho, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(obsSen, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for i in range(6):
        GPIO.setup(stepperPin[i - 1], GPIO.OUT)
    for i in range(3):
        GPIO.setup(lmtSwitch[i - 1], GPIO.IN)
        GPIO.output(stepperPin[i*2], GPIO.HIGH)
    stepperInit()
    UI.videoPage(browser)
    return True
    

def stepperInit():
    '步进电机初始化'
    for i in range(3):
        while GPIO.input(lmtSwitch[i-1]) == GPIO.HIGH:
            stepperCtrl(i)
        print(i,"号电机复位成功")
    devPos = 0

#============================
def btnPressed():
    if GPIO.input(btnPin) == GPIO.HIGH:
        result = True
    else:
        result = False
    return result

def stepperCtrl(stepperID):
    '步进电机基础控制，传入电机编号'
    GPIO.output(stepperPin[(stepperID -1)*2], GPIO.HIGH)
    time.sleep(0.0006)
    GPIO.output(stepperPin[(stepperID -1)*2], GPIO.LOW)
    time.sleep(0.0006)

def stepMoveBack(stepperID, dis):
    '电机往复运动'
    GPIO.output(stepperPin[(stepperID-1)*2], GPIO.HIGH)
    for i in range(dis):
        stepperCtrl(stepperID)
    GPIO.output(stepperPin[(stepperID-1)*2], GPIO.LOW)
    for i in range(dis):
        stepperCtrl(stepperID)

def crush():
    '执行压缩'
    stepMoveBack(1, 1600)

def throw():
    '执行投掷'
    stepMoveBack(3, 1600)

def move2pos(angle):
    '旋转到指定位置'
    if angle >= 0:
        GPIO.output(stepperPin[3], GPIO.HIGH)
    elif  angle < 0:
        GPIO.output(stepperPin[3], GPIO.LOW)
    for i in range(int(angle * 190 / 16.2)):
        stepperCtrl(2)
    

def deltaPos(start, end):
    if end >= 360:
        end = end - 360

    if abs(end - start) <= 180:
        delta = end - start
    else:
        if end > start:
            delta = end - start - 360
        else:
            delta = 360 - start + end
    devPos = end
    return delta

def urtalSonic():
    '超声波测距'
    GPIO.output(usPin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(usPin, GPIO.LOW)
    while not GPIO.input(usEcho):
        pass
    t1 = time.time()
    while GPIO.input(usEcho):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 / 2

def type2id(objType):
    if objType == '可回收物':
        return 0
    elif objType == '厨余垃圾':
        return 1
    elif objType == '其他垃圾':
        return 2
    elif objType == '有害垃圾':
        return 3

def obsSens():
    if GPIO.input(obsSens) == GPIO.LOW:
        return True
    else:
        return False

#====================
def depthDeteced(objType):
    '检测当前桶深'
    emptDis = 400
    objID = type2id(objTpye)
    move2pos(deltaPos(devPos, objID * 90 + 10))
    dis = urtalSonic()
    res = emptDis - dis
    if res < 0:
        res = 0
    else:
        pass
    return res

def moveAndThrow(objTpye):
    UI.waitingPage(browser, '分类ing……')
    objID = type2id(objTpye)
    move2pos(deltaPos(devPos, objID * 90) + 5)
    UI.waitingPage(browser, '投递ing……')
    throw()




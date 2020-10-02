import objectRecogni
import RPi.GPIO as GPIO
import sys
import time
import UIExecutor as UI
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

btnPin = 13

#--------------1-----2-----3
#-------------压缩---旋转---投放
#------------s--r--s---r--s--r
stepperPin = [1, 1, 1 ,1 ,1 ,1]

devPos = 0

def devInit():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for i in range(len(stepperPin)):
        GPIO.setup(stepperPin[i - 1], GPIO.OUT)
    for i in range(3):
        GPIO.output(stepperPin[i*2], GPIO.HIGH)
    

def stepperInit():
    '步进电机初始化'
    pass

#============================
def btnPressed():
    if GPIO.input == GPIO.HIGH:
        result == True
    else:
        result == False
    return result

def updatePage(input):
    '更新UI界面'
    with open("ui.html","w") as f:
        f.write(input)

def stepperCtrl(stepperID):
    '步进电机基础控制，传入电机编号'
    GPIO.output(stepperPin[(stepperID -1)*2], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(stepperPin[(stepperID -1)*2], GPIO.LOW)
    time.sleep(0.5)

def stepMoveBack(stepperID, dis):
    '电机往复运动'
    GPIO.output(stepperPin[stepperID*2], GPIO.HIGH)
    for i in dis:
        stepperCtrl(stepperID)
    GPIO.output(stepperPin[stepperID*2], GPIO.LOW)
    for i in dis:
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
    for i in angle * 190 / 16.2:
        stepperCtrl(2)
    devPos = devPos + angle
    

def deltaPos(start, end):

    return delta

def urtalSonic():
    '超声波测距'
    return distance

def type2id(objTpye):
    if objType == '可回收物':
        return 0
    elif objTpye == '厨余垃圾':
        return 1
    elif objTpye == '其他垃圾':
        return 2
    elif objTpye == '有害垃圾':
        return 3

#====================
def depthDeteced():
    '检测当前桶深'
    emptDis = 40
    move2pos(deltaPos(devPos, objID * 90 + 10))
    dis = urtalSonic()
    return emptDis - dis

def moveAndThrow(objTpye):
    UI.waitingPage(browser, '分类ing……')
    objID = type2id(objTpye)
    move2pos(deltaPos(devPos, objID * 90))
    UI.waitingPage(browser, '投递ing……')
    throw()




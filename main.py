import time
import extension as ex
import UIExecutor as UI
import objectRecogni as OR
import RPi.GPIO as GPIO
import os
import sys
import re

btnState = False
devFull = False

#idBuffer = 0
#typeBuffer = ''

initT = ex.devInit()
#----------可回收物---厨余垃圾---其他垃圾---有害垃圾
#----------容量-个数--容量-个数--容量-个数--容量-个数
devInfo = [  0,  0,   0,  0,   0,  0,   0,  0]

try:
    while initT == True:
        if btnState == False:
            btnState = ex.btnPressed()
        elif btnState == True and devFull == True:
            UI.waitingPage(ex.browser, '等待设备反馈……')
            if ex.obsSens():
                UI.warningPage(ex.browser, '已满，未更换，请联系工作人员！')
            else:
                devFull = False
                UI.videoPage(ex.browser)
            btnState = False
            #devInfo[idBuffer] = ex.depthDeteced(typeBuffer)
        elif btnState == True and devFull == False:
            # main logic
            print('start')
            os.system("fswebcam -s 10 --no-banner -r 640x480 --save res/or_input_res/seg_pred/image.jpg")
            UI.waitingPage(ex.browser, '正在识别，请稍后……')
            objName = OR.pred_name()
            objType = ex.name2type(objName)    #此处更换
            #typeBuffer = objType
            UI.outputPage(ex.browser, objName, objType)
            time.sleep(6)
            if objType == '可回收物':
                UI.waitingPage(ex.browser, '正在压缩……')
                ex.crush()
                ex.moveAndThrow(objType)
            else:
                ex.moveAndThrow(objType)
            UI.waitingPage(ex.browser, '等待设备反馈……')
            typeID = ex.type2id(objType) * 2
            #idBuffer = typeID
            devInfo[typeID] = ex.depthDeteced(objType)
            devInfo[typeID + 1] = devInfo[typeID + 1] + 1
            UI.devInfoPage(ex.browser, devInfo)
            time.sleep(6)
            #if devInfo[typeID] >= 90 and ex.obsSens():
            if ex.obsSens():
                UI.warningPage(ex.browser, '垃圾箱已满，请联系工作人员！')
                devFull = True
            else:
                UI.videoPage(ex.browser)
            btnState = False
finally:
    GPIO.cleanup()
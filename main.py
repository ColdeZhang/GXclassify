import time as sleep
import extension as ex
import UIExecutor as UI
import objectRecogni
import RPi.GPIO as GPIO

# devInfo = ['16','7','32','6','78','15','2','4']

# brow = UI.init()
# time.sleep(1)
# UI.videoPage(brow)
# time.sleep(2)
# UI.waitingPage(brow, '测试中……')
# time.sleep(4)
# UI.outputPage(brow, objectRecogni.OR(), '厨余垃圾')
# #time.sleep(16)
# #UI.devInfoPage(brow,devInfo)

btnState = False

initT = ex.devInit()
#----------可回收物---厨余垃圾---其他垃圾---有害垃圾
#----------容量-个数--容量-个数--容量-个数--容量-个数
devInfo = [  0,  0,   0,  0,   0,  0,   0,  0]

try:
    while initT == True:
        if btnState == False:
            btnState = ex.btnPressed()        
        elif btnState == True:
            # main logic
            print('start')
            UI.waitingPage(ex.browser, '正在识别，请稍后……')
            objName = OR.ans()
            objType = OR.ans()
            UI.outputPage(ex.browser, objName, objType)
            if objType == '可回收物':
                UI.waitingPage(ex.browser, '正在压缩……')
                ex.crush()
                ex.moveAndThrow(objType)
            else:
                ex.moveAndThrow(objType)
            UI.waitingPage(ex.browser, '等待设备反馈……')
            typeID = ex.type2id(objType) * 2
            devInfo[typeID] = ex.depthDeteced(objType)
            devInfo[typeID + 1] = devInfo[typeID + 1] + 1
            UI.devInfoPage(devInfo)
            sleep(6)
            UI.videoPage(ex.browser)
            btnState = False
finally:
    GPIO.cleanup()
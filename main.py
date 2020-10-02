import sys
import time
import extension
import RPi.GPIO as GPIO
import UIExecutor as UI
import objectRecogni

devInfo = ['16','7','32','6','78','15','2','4']

brow = UI.init()
time.sleep(1)
UI.videoPage(brow)
time.sleep(2)
UI.waitingPage(brow, '测试中……')
time.sleep(4)
UI.outputPage(brow, objectRecogni.OR(), '厨余垃圾')
#time.sleep(16)
#UI.devInfoPage(brow,devInfo)



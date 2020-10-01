import sys
import time
import extension
import RPi.GPIO as GPIO
import UIExecutor as UI


brow = UI.init()
time.sleep(1)
UI.videoPage(brow)
time.sleep(1)
UI.waitingPage(brow, '测试中……')
time.sleep(4)
UI.outputPage(brow, '某垃圾', '有害垃圾')

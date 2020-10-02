import objectRecogni
import RPi.GPIO as GPIO
import sys
import time
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

def updatePage(input):
    '更新UI界面'
    with open("ui.html","w") as f:
        f.write(input)

def stepperInit():
    '步进电机初始化'
    pass

def stepperCtrl(length):

    '步进电机运动控制，传入运动距离'
    pass

def depthDeteced():
    '检测当前桶深'
    pass

def crush():
    '执行压缩'
    pass

def throw():
    '执行投掷'
    pass

def move2type(type):
    '旋转到指定类型'
    pass


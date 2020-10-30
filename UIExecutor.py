import sys
import time
from selenium import webdriver
import webbrowser

def init():
    '初始化UI界面'
    updatePage('')
    brow = webdriver.Firefox()
    brow.maximize_window()    #最大化窗口
    brow.get('file:///home/pi/Desktop/GXclassify/ui.html')    #打开地址
    brow.refresh()    #刷新打开的页面
    return brow
    #driver.close()     #关闭浏览器


def videoPage(brow):
    '宣传视频播放界面'
    #<video width="320" height="240" controls><source src="res/UI_res/movie.webm" type="video/webm"></video>
    updatePage('<html><body bgcolor="black"><span ></span><h1 style="color: #ffffff">工程训练自动垃圾分类系统</h1><p>&nbsp;</p><div style="text-align: center; width: 100% "><video width="65%" muted autoplay="autoplay" loop="loop"><source src="res/UI_res/video.webm" type="video/webm"></video></div></body></html>')
    brow.refresh()
    pass

def waitingPage(brow, waitMsg):
    '等待即加载界面，传入加载时提示的信息'
    updatePage('<html><body bgcolor="black"><span ></span><h1 style="color: #ffffff">工程训练自动垃圾分类系统</h1><p>&nbsp;</p><div style="height: 10%"></div><div style="text-align: center; width: 100% "><img src="res/UI_res/loading1.gif" width="40%"  alt=""/></div><div style="font-size: 30px; text-align: center; font-style: inherit; font-weight: bold;color: #ffffff">{}</div></body></html>'.format(waitMsg))
    brow.refresh()
    pass

def warningPage(brow, warnMsg):
    '警告页面'
    updatePage('<html><body bgcolor="black"><span ></span><h1 style="color: #ffffff">工程训练自动垃圾分类系统</h1><p>&nbsp;</p><div style="height: 10%"></div><div style="text-align: center; width: 100% "><img src="res/UI_res/warning.png" width="15%"  alt=""/></div><div style="font-size: 30px; text-align: center; font-style: inherit; font-weight: bold;color: #ffffff">{}</div></body></html>'.format(warnMsg))
    brow.refresh()
    pass

def outputPage(brow, objectName, trashType):
    '展示放入垃圾的类型，传入识别出的垃圾类型'
    updatePage('<html><body bgcolor="black"><span ></span><h1 style="color: #ffffff">工程训练自动垃圾分类系统</h1><p>&nbsp;</p><div class="container-fluid"><div class="row-fluid"><div class="span7" style="width: 50%; margin-left: 5% ; float: left; height: 80%"><img src="res/or_input_res/seg_pred/seg_pred/image.jpg" width="100%"  alt=""/> </div><div class="span5" style="width: 40%; margin-right: 5%; float: left; height: 80%"><div class="row-fluid"><div class="span12" style="text-align: center; width: inherit;height: 30%;line-height: 250px;font-size: 100px;color: #FFFFFF">{}</div></div><div class="row-fluid" ><div class="span4" style="margin-left: 5%; width: 45%; float: left; text-align: center; height: 70%; line-height: 600px; font-size: 60px; font-weight: 500; color: #FFFFFF">属于</div><div class="span8" style="margin-right: 5%; width: 45%; float: left; text-align: center;;margin-top: 15%"><img src="res/UI_res/{}.png" width="100%"alt=""/> </div></div></div></div></div></body></html>'.format(objectName, trashType, trashType))
    brow.refresh()
    pass

def devInfoPage(brow, devInfo):
    '垃圾桶设备情况'
    bar = [str(100 - devInfo[0]),str(100 - devInfo[2]),str(100 - devInfo[4]),str(100 - devInfo[6])]
    updatePage('<html><body bgcolor="black"><span ></span><h1 style="color: white">工程训练自动垃圾分类系统</h1><h1 style="color: white; font-size: 50px">投放成功！</h1><p>&nbsp;</p><div class="container-fluid"><div class="row-fluid"><div class="span12"><div class="row-fluid"><div class="span3" style="float: left; width: 20%; margin-left: 4%;height: 70%;margin-top: 5%"><div class="row-fluid"><div class="span12" style="height: 15%; text-align: center; line-height: 80px; font-size: 40px; font-weight: 400; color: white">可回收物</div></div><div class="row-fluid"><div class="span12" style="height: 65%"><div style="background-color: aqua;width: 100%; height: 100% "><div style="background-color: black;margin : 2%; width: 96%; height: {}%"></div></div></div></div><div class="row-fluid"><div class="span12" style="height: 20%"><div class="row-fluid"><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left"><div style="color: white">当前占用:</div><div style="color: white; font-size: 30px;text-align: end">{}%</div></div><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left;margin-left: 15%"><div style="color: white">统计个数:</div><div style="color: white; font-size: 30px; text-align: end">{}个</div></div></div></div></div></div><div class="span3" style="float: left; width: 20%; margin-left: 4%;height: 70%;margin-top: 5%"><div class="row-fluid"><div class="span12" style="height: 15%; text-align: center; line-height: 80px; font-size: 40px; font-weight: 400; color: white">厨余垃圾</div></div><div class="row-fluid"><div class="span12" style="height: 65%"><div style="background-color:aquamarine;width: 100%; height: 100% "><div style="background-color: black;margin : 2%; width: 96%; height: {}%"></div></div></div></div><div class="row-fluid"><div class="span12" style="height: 20%"><div class="row-fluid"><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left"><div style="color: white">当前占用:</div><div style="color: white; font-size: 30px;text-align: end">{}%</div></div><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left;margin-left: 15%"><div style="color: white">统计个数:</div><div style="color: white; font-size: 30px; text-align: end">{}份</div></div></div></div></div></div><div class="span3" style="float: left; width: 20%; margin-left: 4%;height: 70%;margin-top: 5%"><div class="row-fluid"><div class="span12" style="height: 15%; text-align: center; line-height: 80px; font-size: 40px; font-weight: 400; color: white">其他垃圾</div></div><div class="row-fluid"><div class="span12" style="height: 65%"><div style="background-color:bisque;width: 100%; height: 100% "><div style="background-color: black;margin : 2%; width: 96%; height: {}%"></div></div></div></div><div class="row-fluid"><div class="span12" style="height: 20%"><div class="row-fluid"><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left"><div style="color: white">当前占用:</div><div style="color: white; font-size: 30px;text-align: end">{}%</div></div><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left;margin-left: 15%"><div style="color: white">统计个数:</div><div style="color: white; font-size: 30px; text-align: end">{}份</div></div></div></div></div></div><div class="span3" style="float: left; width: 20%; margin-left: 4%;height: 70%;margin-top: 5%"><div class="row-fluid"><div class="span12" style="height: 15%; text-align: center; line-height: 80px; font-size: 40px; font-weight: 400; color: white">有害垃圾</div></div><div class="row-fluid"><div class="span12" style="height: 65%"><div style="background-color:palevioletred;width: 100%; height: 100% "><div style="background-color: black;margin : 2%; width: 96%; height: {}%"></div></div></div></div><div class="row-fluid"><div class="span12" style="height: 20%"><div class="row-fluid"><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left"><div style="color: white">当前占用:</div><div style="color: white; font-size: 30px;text-align: end">{}%</div></div><div class="span6" style="margin-top: 5%; width: 40%;height: 90%; float: left;margin-left: 15%"><div style="color: white">统计个数:</div><div style="color: white; font-size: 30px; text-align: end">{}个</div></div></div></div></div></div></div></div></div></div></body></html>'.format(bar[0],devInfo[0],devInfo[1],bar[1],devInfo[2],devInfo[3],bar[2],devInfo[4],devInfo[5],bar[3],devInfo[6],devInfo[7]))
    brow.refresh()
    pass

def updatePage(input):
    '更新UI界面'
    with open("ui.html","w") as f:
        f.write(input)



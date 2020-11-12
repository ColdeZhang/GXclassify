# change ACM number as found from ls /dev/tty/ACM*
import UIExecutor as UI
import serial

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600

browser = UI.init()

while True:
    read_ser = ser.readline()
    print(read_ser)
    if(read_ser == "playvideo"):
        UI.videoPage(browser)
    elif(read_ser == "youhailaji"):
        UI.waitingPage(browser, '这是有害垃圾')
    elif(read_ser == "qitalaji"):
        UI.waitingPage(browser, '这是其他垃圾')
    elif(read_ser == "kehuishouwu"):
        UI.waitingPage(browser, '这是可回收物')
    elif(read_ser == "chuyulaji"):
        UI.waitingPage(browser, '这是厨余垃圾')
    elif(read_ser == "manzaijiance"):
        UI.waitingPage(browser, '检测容量中……')
    elif(read_ser == "fenleiwancheng"):
        UI.warningPage(browser, '分类完成！')
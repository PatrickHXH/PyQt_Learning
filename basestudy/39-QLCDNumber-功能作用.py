from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        lcd = QLCDNumber(5,self)
        lcd.move(0,0)
        lcd.resize(300,100)
        # lcd.setDigitCount(6)
        # lcd.display("123456")
        lcd2 = QLCDNumber(self)
        lcd2.move(0,100)
        lcd2.resize(300,100)

        lcd3 = QLCDNumber(self)
        lcd3.move(0,200)
        lcd3.resize(300,100)

        lcd.display(99)
        lcd2.display(99)
        lcd3.display(99)
        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)
        # lcd.setMode(QLCDNumber.Bin) #二进制
        # lcd.setMode(QLCDNumber.Oct) #八进制
        # lcd.setMode(QLCDNumber.Hex) #八进制

        #数值溢出信号
        # lcd.overflow.connect()



        btn =QPushButton(self)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(lcd.value()))
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
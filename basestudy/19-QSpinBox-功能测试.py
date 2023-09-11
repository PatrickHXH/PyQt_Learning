from PyQt5.Qt import *
import sys
class SB(QSpinBox):
    def textFromValue(self, p_int):
        print(p_int)
        return str(p_int) + "*" + str(p_int)

class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        sb  =SB(self)
        self.sb = sb
        sb.resize(100,25)
        sb.move(100,100)
        sb.valueChanged[str].connect(lambda val: print(type(val), val))

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(150,150)
        # btn.clicked.connect(lambda :self.数值循环())
        # btn.clicked.connect(lambda :self.步长设置())
        # btn.clicked.connect(lambda :self.前缀和后缀())
        # btn.clicked.connect(lambda :self.显示的进制设置())
        btn.clicked.connect(lambda :self.设置以及获取数值())
    def 设置以及获取数值(self):
        # self.sb.setRange(0, 9)
        self.sb.setPrefix("撩课")
        # self.sb.setValue(66)
        print(self.sb.value())
        print(self.sb.text())
        print(self.sb.lineEdit().text())
        pass

    def 显示的进制设置(self):
        print(self.sb.displayIntegerBase())
        self.sb.setDisplayIntegerBase(2)
        print(self.sb.displayIntegerBase())
    def 前缀和后缀(self):
        # self.sb.setRange(1,12)
        # self.sb.setSuffix("月")
        self.sb.setRange(0, 6)
        self.sb.setPrefix("周")
        self.sb.setSpecialValueText("周日")
    def 步长设置(self):
        self.sb.setSingleStep(3)
    def 数值循环(self):
        print(self.sb.wrapping())
        self.sb.setWrapping(True)
        print(self.sb.wrapping())

    def 最大值最小值(self):
        # self.sb.setMaximum(180)
        # print(self.sb.maximum())

        # self.sb.setMinimum(18)
        # print(self.sb.minimum())
        self.sb.setRange(18, 180)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
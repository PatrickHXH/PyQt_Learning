from PyQt5.Qt import *
import sys
class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        print("xxxxx", p_float)
        # return str(p_float) + "*" + str(p_float)

class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        dsb = MyDoubleSB(self)
        dsb.move(100, 100)
        dsb.resize(100, 30)

        # dsb.setMaximum(88.88)
        # dsb.setSingleStep(0.02)
        # dsb.setSuffix("倍速")
        # dsb.setWrapping(True) #循环
        # dsb.setSpecialValueText("正常")
        # dsb.setDecimals(1)  #保留小数

        test_btn = QPushButton(self)
        test_btn.move(300,300)
        test_btn.setText("测试按钮")
        # test_btn.clicked.connect(lambda :dsb.setValue(-166.66))
        # test_btn.clicked.connect(lambda :print(type(dsb.value()), dsb.value()))
        # test_btn.clicked.connect(lambda :print(type(dsb.cleanText()), dsb.cleanText()))
        # test_btn.clicked.connect(lambda :print(type(dsb.text()), dsb.text()))
        test_btn.clicked.connect(lambda :print(type(dsb.lineEdit().text()), dsb.lineEdit().text()))

        dsb.valueChanged.connect(lambda val:print(val,type(val)))
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
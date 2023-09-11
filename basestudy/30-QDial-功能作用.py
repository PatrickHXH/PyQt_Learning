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
        label = QLabel(self)
        label.move(200, 100)
        label.setText("社会我顺哥, 人狠话不多")

        # 展示内容
        dia = QDial(self)

        dia.setRange(0,200)
        # dia.valueChanged.connect(lambda val:print("值发生了改变：",val))
        def test(val):
            label.setStyleSheet("font-size: {}px;".format(val))
            label.adjustSize()
        dia.valueChanged.connect(test)
        dia.setNotchesVisible(True)  #启用刻度线
        dia.setPageStep(5)

        dia.setWrapping(True)
        dia.setNotchTarget(50)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
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
        lablel = QLabel("0",self)
        lablel.move(200,200)
        lablel.resize(100,30)
        sd = QSlider(self)
        sd.move(100,100)
        # sd.valueChanged.connect(lambda val:lablel.setText(str(val)))
        sd.valueChanged.connect(lambda :lablel.setText(str(sd.value())))

        # 设置最大值 最小值
        sd.setMaximum(100)
        sd.setMinimum(66)

        #当前数值
        # sd.setValue(88)

        # 步长设置
        sd.setSingleStep(5)
        sd.setPageStep(8)

        # 跟踪设置
        # print(sd.hasTracking())
        # sd.setTracking(False)

        # 滑块位置的设置
        sd.setSliderPosition(88)

        # 倒立外观
        sd.setInvertedAppearance(True)
        sd.setInvertedControls(True)
        # sd.setOrientation(Qt.Horizontal)

        #信号
        # sd.sliderMoved.connect(lambda val:print(val))
        # sd.actionTriggered.connect(lambda  val:print(val))
        sd.rangeChanged.connect(lambda min,max:print(min,max))

        sd.setMaximum(99)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
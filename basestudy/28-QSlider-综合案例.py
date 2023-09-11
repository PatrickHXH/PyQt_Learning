from PyQt5.Qt import *
import sys
class Slider(QSlider):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setup_ui()
    def setup_ui(self):
        self.lablel = QLabel(self)
        self.lablel.setText("0")
        self.lablel.setStyleSheet("color: red;")
        self.lablel.hide()

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        x = (self.width() - self.lablel.width()) / 2
        # y / height = （最大值 - 最小值 - 当前值） / (最大值 - 最小值)
        #
        # y / height = 1 - 当前值 / (最大值 - 最小值)
        #
        # y = (1 - 当前值 / (最大值 - 最小值)) * height
        print("当前值：",self.value())
        print("最大值：",self.maximum())
        print("最小值：",self.minimum())
        y = (1 - self.value() / (self.maximum() - self.minimum())) * self.height() - self.lablel.height()
        print(x,y)
        self.lablel.move(int(x),int(y))

    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt)
        x = (self.width() - self.lablel.width()) / 2
        # y / height = （最大值 - 最小值 - 当前值） / (最大值 - 最小值)
        #
        # y / height = 1 - 当前值 / (最大值 - 最小值)
        #
        # y = (1 - 当前值 / (最大值 - 最小值)) * height
        y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.lablel.height())
        self.lablel.show()
        self.lablel.move(int(x),int(y))
        self.lablel.setText(str(self.value()))
        self.lablel.adjustSize()
    def mouseReleaseEvent(self, evt):
        super().mouseReleaseEvent(evt)
        self.label.hide()
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
        self.set_ui()
    def set_ui(self):
        # 展示内容
        slider = Slider(self)
        slider.move(200,200)
        slider.resize(30,200)
        slider.setTickPosition(QSlider.TicksBothSides)



if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
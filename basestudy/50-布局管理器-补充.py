from PyQt5.Qt import *
import sys
class Label(QLabel):
    # def minimumSizeHint(self):
    #     return QSize(200,200)
    def sizeHint(self):
        return QSize(150,60)
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(500,500)

    def set_ui(self):
        # 展示内容
        label1 = Label("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum)
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Preferred)
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)  #expanding优先级比preferred高
        sp = QSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        sp.setRetainSizeWhenHidden(True)   #标签隐藏时显示标签区域
        label1.setSizePolicy(sp)
        # label1.hide()
        label1.setFixedSize(200,200)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
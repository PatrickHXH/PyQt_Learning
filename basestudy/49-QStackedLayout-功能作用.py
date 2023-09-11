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
        sl = QStackedLayout()
        self.setLayout(sl)
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label1.setStyleSheet("background-color:cyan")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:cyan")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:yellow")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:red")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        print(sl.addWidget(label1))
        print(sl.addWidget(label2))
        print(sl.addWidget(label3))

        print(sl.insertWidget(10, label5))
        print(sl.widget(3).text())
        # sl.setCurrentIndex(2)

        # timer = QTimer(self)
        # timer.timeout.connect(lambda :sl.setCurrentIndex(sl.currentIndex() + 1 % sl.count()))
        # timer.start(1000)
        #信号
        # sl.currentChanged.connect(lambda val:print(val))

        # sl.setStackingMode(QStackedLayout.StackAll)
        label1.setFixedSize(100,100)
        label2.setFixedSize(150,150)
        sl.removeWidget(label1)
        sl.removeWidget(label2)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作

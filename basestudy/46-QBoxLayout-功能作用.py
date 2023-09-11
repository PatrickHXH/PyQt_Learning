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
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label1.setStyleSheet("background-color:cyan")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        layout = QBoxLayout(QBoxLayout.LeftToRight)

        self.setLayout(layout)
        layout.addWidget(label1)
        # layout.addSpacing(100)  #设置间距
        # layout.addStretch(2)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.setStretchFactor(label2,1)

        # layout.insertSpacing(3,60)
        # timer = QTimer(self)
        # def test():
        #     layout.setDirection((layout.direction()+1) %4 )
        # timer.timeout.connect(test)
        # timer.start(1000)

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:cyan")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:yellow")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:red")

        # h_layout = QBoxLayout(QBoxLayout.TopToBottom)
        h_layout = QVBoxLayout()
        h_layout.addWidget(label5)
        h_layout.addWidget(label6,1)
        h_layout.addWidget(label7)
        layout.addLayout(h_layout,1)
        # layout.insertLayout(2,h_layout)

        # layout.removeWidget(label1)
        # label1.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
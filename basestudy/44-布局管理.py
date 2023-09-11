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

        # label_width = int(self.width())
        # label_height = int(self.height() /3 )
        # label1.resize(label_width,label_height)
        # label2.resize(label_width,label_height)
        # label3.resize(label_width,label_height)
        #
        # label1.move(0,0)
        # label2.move(0,label_height)
        # label3.move(0,label_height * 2)

        #定时器
        # timer = QTimer(self)
        # timer.timeout.connect(lambda :label1.setText(label1.text() + "itlike\n"))
        # timer.start(1000)

        #布局管理器
        # v_layout = QVBoxLayout()
        v_layout = QHBoxLayout()
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)
        v_layout.setContentsMargins(20,30,40,50)  #框架间距
        v_layout.setSpacing(60)
        self.setLayout(v_layout)
        self.setLayoutDirection(Qt.RightToLeft)
        # label2.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
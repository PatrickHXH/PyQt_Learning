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
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label1.setStyleSheet("background-color:cyan")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")
        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        #1.创建一个布局管理器对象
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        #2.直接把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)
        #3.把需要布局的子控件添加到布局管理器当中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        # layout.setSpacing(60)

        print(layout.contentsMargins().left())
        print(layout.contentsMargins().right())
        # layout.setContentsMargins(20,40,60,80)

        layout.replaceWidget(label2,label4)
        label2.hide()

        label2.destroyed.connect(lambda :print("标签2被释放"))
        label2.setParent(None)
        print(label2.parent())

        #布局的嵌套
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:cyan")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:yellow")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:red")

        h_layout = QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)

        #把需要布局的子控件添加到布局管理器当中
        layout.addWidget(label1)
        layout.addLayout(h_layout)
        layout.addWidget(label2)
        layout.addWidget(label3)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
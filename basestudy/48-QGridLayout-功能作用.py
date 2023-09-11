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
        gl = QGridLayout()
        self.setLayout(gl)
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label1.setStyleSheet("background-color:cyan")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        gl.addWidget(label1,0,0)
        gl.addWidget(label2,0,1)
        gl.addWidget(label3,1,0,3,3)  #1行 0列  3行3列

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
        gl.addLayout(v_layout,4,0)   #4行 0列

        print(gl.getItemPosition(1))
        print(gl.itemAtPosition(0, 1).widget())

        # gl.setColumnStretch(0,1)  #第0列伸缩因子为1
        # gl.setColumnStretch(1,2)  #第1列伸缩因子为2
        # gl.setRowStretch(4,1)

        print(gl.spacing())
        # print(gl.verticalSpacing())  #垂直间距
        # print(gl.horizontalSpacing())  #水平间距
        # gl.setVerticalSpacing(60)  #设置垂直间距
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    gl = window.layout()
    print(gl.cellRect(0, 1))
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
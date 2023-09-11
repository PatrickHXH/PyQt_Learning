from PyQt5.Qt import *
import sys

'''
.QLabel {
    background-color:pink;
}
.QLabel[notice_level='error'] {
    border:3px solid red
 }
 .QLabel[notice_level='warning'] {
    border:3px solid yellow
 }
'''
class Btn(QPushButton):
    pass
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        box1 =QWidget(self)
        box2 = QWidget(self)
        # box1.setStyleSheet("QPushButton {background-color:orange;}")
        box2.setObjectName("box2")

        box3 = QWidget(box2)
        box3.resize(150,150)

        # box2.setStyleSheet("background-color:cyan")
        label1 = QLabel("标签1",box1)
        label1.resize(300,60)
        # label1.setObjectName("pink")
        label1.setProperty("notice_level","warning")
        label1.move(50,50)
        btn1 =Btn("按钮1",box1)
        btn1.move(150,50)

        cb = QCheckBox("python",box1)
        cb.move(150,200)
        cb.resize(100,100)
        cb.setTristate(True)

        label2 = QLabel("标签2",box3)
        label2.resize(100, 60)
        label2.move(50,50)
        label2.setProperty("notice_level", "error")

        label3 = QLabel("标签3",box2)

        btn2 =QPushButton("按钮2",box2)
        btn2.move(150,50)
        btn2.setObjectName("b2")
        btn2.setDisabled(True)

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.addWidget(box1)
        v_layout.addWidget(box2)

        # self.other_btn = QPushButton("按钮3")
        # self.other_btn.show()
        # self.setStyleSheet("QPushButton {background-color:orange;}")

if __name__ == '__main__':
    import sys
    from Tool import QSSTool
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    QSSTool.setQssToObj("test.qss",app)
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
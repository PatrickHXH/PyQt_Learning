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
        btn = QPushButton("测试按钮",self)
        btn.setObjectName("btn")
        btn.resize(200,200)
        btn.move(100,100)

        btn2 = QPushButton("测试按钮",self)
        btn2.setObjectName("btn2")
        btn2.resize(200,200)
        btn2.move(100,300)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot(bool)
    def on_btn_clicked(self,val):
        print("按钮被点击了",val)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
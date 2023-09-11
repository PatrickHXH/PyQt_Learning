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
        from PyQt5.uic import loadUi
        loadUi("class_ts.ui",self)


if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    print(dir(window))
    def click():
        print("xxx")
        account = window.lineEdit.text()
        pwd = window.lineEdit_2.text()
        print(account,pwd)
    window.pushButton.clicked.connect(click)
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
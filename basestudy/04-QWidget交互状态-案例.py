from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(500,500)

    def set_ui(self):
        # 添加三个子控件
        label = QLabel(self)
        label.setText("标签")
        label.move(100,50)
        label.setHidden(True)

        le = QLineEdit(self)
        le.move(100,100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100,150)
        btn.setEnabled(False)

        def text_cao(text):
            print("文本内容发生了改变",text)
            btn.setEnabled(len(text)>0)
        le.textChanged.connect(text_cao)

        def check():
            content = le.text()
            if content =="Sz":
                label.setText("登录成功")
            else:
                label.setText("登录失败")
            label.show()
            label.adjustSize()

        btn.pressed.connect(check)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
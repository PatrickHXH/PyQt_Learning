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
        # background - origin: content;
        # background - clip: padding;
        # 展示内容
        self.setStyleSheet("""
        QPushButton{
            background-image:url(./test01.jpg);
            border:20px double red;
            background-origin: content;
            background-clip: padding;
        }
        """)
        h_layout =QHBoxLayout(self)
        for i in range(0,13):
            btn = QPushButton(self)
            btn.setFixedSize(140,140)
            btn.setStyleSheet("""
            QPushButton{
                padding-left:-%dpx
            }
            """%(i*50))
            h_layout.addWidget(btn)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
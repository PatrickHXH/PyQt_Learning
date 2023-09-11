from PyQt5.Qt import *
import sys
from class_ts import Ui_Form
class Window(QWidget,Ui_Form):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
        self.setupUi(self)
    def set_ui(self):
        # 展示内容
        pass
    def btn_click(self):
        print("xxxxx")
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
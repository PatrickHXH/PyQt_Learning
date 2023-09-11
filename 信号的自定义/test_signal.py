from PyQt5.Qt import *
import sys
class Btn(QPushButton):

    rightClicked = pyqtSignal([str],[int,str])
    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        # print(evt.button())
        if evt.button() == Qt.RightButton:
            print("应该发射右键信号")
            self.rightClicked[str].emit(self.text())
            self.rightClicked[int,str].emit(888,"hello")

class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        btn =Btn("XXX",self)
        # btn.rightClicked.connect(lambda :print("按钮被点击了"))
        # btn.pressed.connect(lambda content:print("按钮被点击了",content))
        # btn.rightClicked[str].connect(lambda content:print("按钮被点击了",content))
        # btn.rightClicked[int].connect(lambda content:print("按钮被点击了",content))
        btn.rightClicked[int,str].connect(lambda content,c2:print("按钮被点击了",content,c2))


if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
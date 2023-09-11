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
        sb = QScrollBar(self)
        sb.resize(30,200)
        sb.move(100,100)

        sb2 = QScrollBar(Qt.Horizontal,self)
        sb2.resize(200,30)
        sb2.move(150,100)

        sb.valueChanged.connect(lambda val:print(val))
        sb.setPageStep(50)
        sb.grabKeyboard()
    
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
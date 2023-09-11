from PyQt5.Qt import *
import sys
import qdarkgraystyle
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        layout = QVBoxLayout(self)
        label = QLabel("xxx")
        layout.addWidget(label)

        btn = QPushButton("xx2")
        layout.addWidget(btn)

        cb = QComboBox()
        cb.addItems(["1","2","3"])
        layout.addWidget(cb)

        sb = QSpinBox()
        layout.addWidget(sb)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
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
        kse = QKeySequenceEdit(self)
        # ks = QKeySequence("Ctrl+C")
        # ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        kse.setKeySequence(ks)
        kse.clear()

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(kse.keySequence().toString(), kse.keySequence().count()))

        kse.editingFinished.connect(lambda :print("结束编辑"))
        kse.keySequenceChanged.connect(lambda :print("键位序列发生改变"))
        kse.keySequenceChanged.connect(lambda key_val: print("键位序列发生改变", key_val.toString()))
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序 对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
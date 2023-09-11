import sys
from PyQt5.Qt import *

class Mylabel(QLabel):
    def keyPressEvent(self, evt):
        if evt.modifiers() == Qt.ControlModifier  |  Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print("ctrl + shift + a键被点击了")
app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

label =Mylabel(window)
label.resize(100,100)
label.setStyleSheet("background-color:blue")
label.grabKeyboard()

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




import sys
from PyQt5.Qt import *

class Window(QWidget):
    def mousePressEvent(self, evt):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

app =QApplication(sys.argv)

window = Window()
window.resize(500,500)

#最小化、最大化、全屏
# window.setWindowState(Qt.WindowMinimized)
# window.setWindowState(Qt.WindowMaximized)
#
# window.setWindowState(Qt.WindowActive)

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




import sys
from PyQt5.Qt import *

class Window(QWidget):
    def mousePressEvent(self, evt):
        #聚焦到 下一个子控件
        # self.focusNextChild()
        pass
app =QApplication(sys.argv)

window = Window()
window = QWidget()
window.resize(500,500)

le1 = QLineEdit(window)
le1.move(50,50)

le2 = QLineEdit(window)
le2.move(50,100)

le3 = QLineEdit(window)
le3.move(50,150)

#自定义焦点顺序
window.setTabOrder(le1,le3)
window.setTabOrder(le3,le2)
window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




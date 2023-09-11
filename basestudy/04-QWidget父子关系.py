import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

QLabel(window)
print(window.childAt(50,50))
print(window.childrenRect())



window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




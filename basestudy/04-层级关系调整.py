import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

#层级关系
label1 = QLabel(window)
label2 = QLabel(window)
# label1.lower()
label1.raise_()
label1.stackUnder(label2)



window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

btn =QCommandLinkButton("标题","描述",window)



window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




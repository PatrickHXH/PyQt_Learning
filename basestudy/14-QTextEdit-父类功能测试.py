import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(1500,1500)

te = QTextEdit(window)
te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

btn = QPushButton(window)
te.setCornerWidget(btn)

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




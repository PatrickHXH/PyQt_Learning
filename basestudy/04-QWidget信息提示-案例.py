import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

# window = QWidget()
window = QMainWindow()
window.resize(500,500)
window.statusBar()

label = QLabel(window)
label.setText("社会我瀚哥")
label.setStatusTip("这是标签")
label.setToolTip("这是一个提示标签")
label.adjustSize()
print(label.toolTip())

label.setToolTipDuration(2000)
print(label.toolTipDuration())



window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
cb = QCheckBox("Python",window)
cb.setTristate(True)
cb.setCheckState(Qt.Unchecked)  #没有选中
cb.setCheckState(Qt.PartiallyChecked)  #部分选中
cb.setCheckState(Qt.Checked)  #全部选中
#传递信号
cb.stateChanged.connect(lambda state:print(state))

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




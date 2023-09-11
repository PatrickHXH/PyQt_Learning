import sys
from PyQt5.Qt import *
import ffmpeg

app =QApplication(sys.argv)
window = QWidget()
window.resize(500,500)

le  = QLineEdit(window)
le.move(50,10)
#设置文本框最大长度
# le.setMaxLength(3)

#设置文本是否只可只读
# le.setReadOnly(True)

le2 = QLineEdit(window)
le2.move(50,50)
#设置文本框输出模式
# le2.setEchoMode(QLineEdit.PasswordEchoOnEdit)

#设置掩码，没有输入显示#号
le2.setInputMask(">AA-99;#")
le2.setFocus()

def cao():
    print(le.isModified())

btn =QPushButton("按钮",window)
btn.move(100,100)
# btn.clicked.connect(lambda :le2.setText(le.text()))
btn.clicked.connect(cao)
# btn.pressed.connect(lambda :print())

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




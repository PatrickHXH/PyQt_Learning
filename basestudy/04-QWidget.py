import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)



lable = QLabel(window)
lable.setText("黄侠瀚")
lable.setStyleSheet("background-color: yellow")
def cao():
    new_content = lable.text() + "黄侠瀚"
    lable.setText(new_content)
    lable.adjustSize()

btn = QPushButton(window)
btn.setText("复制按钮")
btn.move(100,100)

btn.clicked.connect(cao)
window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




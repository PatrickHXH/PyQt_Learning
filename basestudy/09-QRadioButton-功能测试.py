import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(500,500)

#新建两个子窗口
yellow = QWidget(window)
yellow.resize(200,200)
yellow.setStyleSheet("background-color:yellow")
yellow.move(50,50)

green = QWidget(window)
green.resize(200,200)
green.setStyleSheet("background-color:green")
green.move(yellow.x()+yellow.width(),yellow.y()+yellow.height())

rb_nan = QRadioButton("男",yellow)
rb_nan.setShortcut("Alt+M")
rb_nan.move(10,50)
rb_nan.setChecked(True)
rb_nv = QRadioButton("女-&Female",yellow)
rb_nv.move(10,100)
# rb_nv.toggled.connect(lambda ischecked:print(ischecked))

#设置按钮排他性，不互斥
# rb_nv.setAutoExclusive(False)

rb_yes = QRadioButton("Yes",green)
rb_yes.move(10,50)
rb_no = QRadioButton("No",green)
rb_no.move(10,100)


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




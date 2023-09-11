import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(1500,1500)

d =QDialog(window)

btn1 = QPushButton(d)
btn1.setText("btn1")
btn1.move(20,20)
btn1.clicked.connect(lambda :d.accept())

btn2 = QPushButton(d)
btn2.setText("btn2")
btn2.move(60, 60)
btn2.clicked.connect(lambda :d.reject())
# btn2.clicked.connect(lambda :print(d.result()))

btn3 = QPushButton(d)
btn3.setText("btn3")
btn3.move(60, 160)
btn3.clicked.connect(lambda :d.done(8))
# btn3.clicked.connect(lambda :d.setResult(888))

d.accepted.connect(lambda :print("点击了, 接受按钮"))
d.rejected.connect(lambda :print("点击了, 拒绝按钮"))
d.finished.connect(lambda val:print("点击了, 完成按钮", val))

d.setWindowTitle("对话框")
# d.setModal(True)   #设置对话框为模态
# d.setWindowModality(Qt.WindowModal)  #设置对话框为模态
# d.show()
# d.setSizeGripEnabled(True)
result = d.exec()
print(result)


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




import sys
from PyQt5.Qt import *

class App(QApplication):
    def notify(self, recevier,evt):
        if recevier.inherits("QPushButton") and evt.type() ==QEvent.MouseButtonPress:
            print(recevier,evt)
        return super().notify(recevier,evt)

class Btn(QPushButton): 
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt,"事件中点击")
        return super().event(evt)

app =App(sys.argv)

window = QWidget()
window.resize(500,500)
btn = Btn(window)
btn.setText("按钮")
def cao():
    print("按钮被点击了")
btn.pressed.connect(cao)
window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




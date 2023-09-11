import sys
from PyQt5.Qt import *

class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText("5")
        self.move(100,100)
        self.setStyleSheet("font-size: 22px")
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        current_sec = int(self.text())
        current_sec -=1
        self.setText(str(current_sec))

        if current_sec ==0:
            print("停止")
            self.killTimer(self.timer_id)
app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

label = MyLabel(window)


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




import sys
from PyQt5.Qt import *

class Window(QWidget):
    def mousePressEvent(self, evt):
        local_x = evt.x()
        local_y = evt.y()
        sub_widget = self.childAt(local_x,local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color:red")
        print("被点击了",local_x,local_y)
app =QApplication(sys.argv)

window = Window()
window.resize(500,500)

for i in range(0,11):
    label = QLabel(window)
    label.setText("标签"+str(i))
    label.move(40*i,40*i)


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




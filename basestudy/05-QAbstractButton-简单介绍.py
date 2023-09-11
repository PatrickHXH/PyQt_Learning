import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

class Btn(QAbstractButton):
    def paintEvent(self, evt):
        #1 创建一个画家，画在什么地方
        painter = QPainter(self)

        #2 给画家一个笔，创建一个笔
        pen = QPen(QColor(111,200,20),5)

        #3 设置这个笔
        painter.setPen(pen)

        #画家画
        painter.drawText(25,40,self.text())
        painter.drawEllipse(0,0,100,100)

btn =Btn(window)
btn.setText("xxx")
btn.resize(100,100)

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




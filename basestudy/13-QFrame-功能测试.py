import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(1500,1500)

frame = QFrame(window)
frame.resize(100,100)
frame.move(100,100)
frame.setStyleSheet("background-color:yellow")

#设置框架形状
# frame.setFrameShape(QFrame.Box)
# frame.setFrameShape(QFrame.Panel)
#设置框架阴影
# frame.setFrameShadow(QFrame.Raised)

frame.setFrameStyle(QFrame.Box | QFrame.Raised)
#设置外线和中线宽度
frame.setLineWidth(6)
frame.setMidLineWidth(12)

#框架x，y轴体，宽高
frame.setFrameRect(QRect(50,50,10,10))
window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




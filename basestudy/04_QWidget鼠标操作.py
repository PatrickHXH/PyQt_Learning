import sys
from PyQt5.Qt import *

class MyWindow(QWidget):
    def mouseMoveEvent(self, me):
        # QMoveEvent
        print("鼠标移动了",me.localPos())
        lablel = self.findChild(QLabel)
        lablel.move(me.localPos().x(),me.localPos().y())
app =QApplication(sys.argv)

window = MyWindow()
window.resize(500,500)
window.setMouseTracking(True)
window.setCursor(Qt.ForbiddenCursor)

#自定义鼠标
# pixmap = QPixmap("xxx.png")
# new_pixmap = pixmap.scaled(50,50)
# Qcursor = QCursor(new_pixmap,0,0)
# window.setCursor(Qcursor)

lable = QLabel(window)
lable.setText("HXH")


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




from PyQt5.Qt import *
import sys
class Btn(QPushButton):
    def hitButton(self, point):
        #通过给定的一个点坐标，计算与圆心的距离
        circle_x = self.width()/2
        circle_y = self.height() /2

        hit_x = point.x()
        hit_y = point.y()
        import math
        distance = math.sqrt(math.pow(hit_x-circle_x,2)+math.pow(hit_y-circle_y,2))
        if distance < self.width() /2:
            return True
        return  False
    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100,150,200),6))
        painter.drawEllipse(self.rect())
        painter.drawEllipse(0,0,300,300)



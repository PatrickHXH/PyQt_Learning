import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

#*************状态设置**************开始
# push_button = QPushButton(window)
# push_button.setText("这是QPushButton")
# push_button.move(100,100)
#
# radio_button = QRadioButton(window)
# radio_button.setText("这是一个radio")
# radio_button.move(100,150)
#
# checkbox = QCheckBox(window)
# checkbox.setText("这是checkbox")
# checkbox.move(100,200)
#
# push_button.setStyleSheet("QPushButton:pressed {background-color:red}")

#设置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)

#检查能否被选中
# print(push_button.isCheckable())
# print(radio_button.isCheckable())
# print(checkbox.isCheckable())

#设置为选中状态
# push_button.setChecked(True)
# radio_button.setChecked(True)
# checkbox.setChecked(True)

#检查是否被选中
# print(push_button.isChecked())
# print(radio_button.isChecked())
# print(checkbox.isChecked())

#*************状态设置**************结束

# ###图标按钮###
# btn = QPushButton(window)
# icon = QIcon("test.png")
# btn.setIcon(icon)
#
# size = QSize(70,70)
# btn.setIconSize(size)
# def btnevent():
#     push_button.toggle()
#     radio_button.toggle()
#     checkbox.toggle()
#
# btn.pressed.connect(btnevent)

###按钮快捷键###
# btn.setShortcut(" Alt+b")

###按钮自动重复###
# btn.setAutoRepeat(True)
# btn.setAutoRepeatDelay(2000)
# btn.setAutoRepeatInterval(1000)


#*************排他性设置**************开始
'''
for i in range(0,3):
    btn = QRadioButton(window)
    btn.setText("btn"+str(i))
    btn.move(50*i,50*i)

    # btn.setAutoExclusive(True)
    print(btn.autoExclusive())
    # btn.setCheckable(True)

btn = QPushButton(window)
btn.setText("btn3")
btn.setCheckable(True)
btn.move(200,200)
'''
#*************排他性设置**************结束

#*************按钮模拟点击**************开始
''' 
btn = QPushButton(window)
btn.setText("这是按钮")
btn.move(200,200)
btn.pressed.connect(lambda :print("点击了这个按钮"))
# btn.click()
btn.animateClick(2000)
'''
#*************按钮模拟点击**************结束

#*************按钮点击有效区域**************开始
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
btn = Btn(window)
btn.setText("按钮")
btn.resize(300,300)
print("xxxx",btn.rect())
btn.move(100,100)
btn.pressed.connect(lambda :print("按钮被点击了"))


#*************按钮点击有效区域**************结束

window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作


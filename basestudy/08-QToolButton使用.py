import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

#*************工具按钮的菜单设置**************开始

tb = QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon("test.png"))
tb.setIconSize(QSize(100,100))
tb.setToolTip("这是一个工具按钮")
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#箭头
tb.setArrowType(Qt.RightArrow)
tb.setAutoRaise(True)

#创建普通按钮
# btn =  QPushButton("一般按钮",window)
# btn.move(100,100)

#创建菜单—>普通按钮
menu =QMenu(tb)

#设置子菜单归属和样式
sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("test.png"))

action = QAction(QIcon("test.png"), "行为", menu)
action.setData([1])
menu.addAction(action)
menu.addSeparator()
menu.addMenu(sub_menu)

#按钮设置菜单
tb.setMenu(menu)
#设置工具按钮的弹出形式
tb.setPopupMode(QToolButton.MenuButtonPopup)
tb.setPopupMode(QToolButton.InstantPopup)
#action点击事件
def do_action(action):
    QAction
    print("点击了行为",action.data())
tb.triggered.connect(do_action)
#*************工具按钮的菜单设置**************结束


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




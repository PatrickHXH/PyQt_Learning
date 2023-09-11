import sys
from PyQt5.Qt import *

class Window(QWidget):
    def contextMenuEvent(self, evt):
        # *************菜单的设置**************开始
        btn = QPushButton(QIcon("test.png"), "xxx", self)
        menu = QMenu(btn)

        # 一级菜单按钮，最近打开—包含二级菜单
        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle("最近打开")

        # 一级菜单按钮，新建
        new_action = QAction(QIcon("test.png"), "新建", menu)
        new_action.triggered.connect(lambda: print("新建文件"))

        # 一级菜单按钮，打开
        open_action = QAction(QIcon("test.png"), "打开", menu)
        open_action.triggered.connect(lambda: print("打开文件"))

        # 一级菜单按钮，退出
        exit_action = QAction(QIcon("test.png"), "退出", menu)
        exit_action.triggered.connect(lambda: print("退出"))

        # 二级菜单

        file_action = QAction("PythonGUI编程", open_recent_menu)

        menu.addAction(new_action)
        menu.addAction(open_action)
        menu.addMenu(open_recent_menu)
        open_recent_menu.addAction(file_action)
        menu.addSeparator()
        menu.addAction(exit_action)

        btn.setMenu(menu)
        # btn.setFlat(True)
        menu.exec_(evt.globalPos())
        print("展示菜单")
        # *************菜单的设置**************结束

app =QApplication(sys.argv)
window = Window()
window.resize(500,500)


#*************默认选中按钮**************开始
'''

btn2 = QPushButton(window)
btn2.setText("按钮2")
btn2.move(150,150)
btn2.setAutoDefault(True)
# btn2.setDefault(True)

# print(btn.autoDefault())
print(btn2.autoDefault())
'''
#*************默认选中按钮**************结束

#*************自定义右键菜单**************开始
'''
def show_menu(point):
    menu = QMenu(window)

    # 一级菜单按钮，最近打开—包含二级菜单
    open_recent_menu = QMenu()
    open_recent_menu.setTitle("最近打开")

    # 一级菜单按钮，新建
    new_action = QAction(QIcon("test.png"), "新建", menu)
    new_action.triggered.connect(lambda: print("新建文件"))

    # 一级菜单按钮，打开
    open_action = QAction(QIcon("test.png"), "打开", menu)
    open_action.triggered.connect(lambda: print("打开文件"))

    # 一级菜单按钮，退出
    exit_action = QAction(QIcon("test.png"), "退出", menu)
    exit_action.triggered.connect(lambda: print("退出"))

    # 二级菜单

    file_action = QAction("PythonGUI编程", open_recent_menu)

    menu.addAction(new_action)
    menu.addAction(open_action)
    menu.addMenu(open_recent_menu)
    open_recent_menu.addAction(file_action)
    menu.addSeparator()
    menu.addAction(exit_action)

    # btn.setMenu(menu)
    # btn.setFlat(True)
    menu.exec_(window.mapToGlobal(point))
window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)
'''
#*************自定义右键菜单**************结束

window.show()
# btn.showMenu()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




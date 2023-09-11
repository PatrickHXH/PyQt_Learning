from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        cb = QComboBox(self)
        cb.resize(400,30)
        cb.addItems(["abc", "123", "456"])
        cb.addItem(QIcon("test.png"), "撩课", {"name": "itllike"})

        btn = QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(cb.count()))
        # btn.clicked.connect(lambda :print(cb.currentIndex()))
        # btn.clicked.connect(lambda :print(cb.currentText()))
        # btn.clicked.connect(lambda :print(cb.currentData()))
        # btn.clicked.connect(lambda : btn.setIcon(cb.itemIcon(cb.currentIndex())))
        # btn.clicked.connect(lambda _, idx = cb.count()-1:print(cb.itemIcon(idx), cb.itemText(idx), cb.itemData(idx)))    #_下划线是忽略
        # btn.clicked.connect(lambda :cb.clear())
        # btn.clicked.connect(lambda :cb.clearEditText())
        # btn.clicked.connect(lambda :cb.showPopup())


        #限制最大显示
        cb.setMaxCount(6)
        cb.setEditable(True)

        # cb.addItem("xx1")
        # cb.addItem("xx2")
        # cb.addItem(QIcon("test.png"),"xx2")
        # cb.addItems(["1","2","3"])

        # cb.insertItem(1,"xxx")
        # cb.setItemIcon(2,QIcon("test.png"))
        # cb.setItemText(2,"社会顺")

        # cb.removeItem(1)
        # cb.insertSeparator(2)  #插入分割线
        # cb.setCurrentIndex(1)  #设置默认显示
        # cb.setCurrentText("社会顺") #设置默认显示

        cb.setEditable(True)  #设置可被编辑
        # cb.setMaxVisibleItems(3)
        # cb.setDuplicatesEnabled(True)
        cb.setDuplicatesEnabled(True)
        cb.setIconSize(QSize(60,60))
        cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)  #自适应内容

        #可迭代对象
        cb.setCompleter(QCompleter(["123", "abc", "aaa", "bbb"]))

        # print(QAbstractItemModel.__subclasses__())
        # model = QStandardItemModel()
        # item1 = QStandardItem("item1")
        # item2 = QStandardItem("item2")
        # item22 = QStandardItem("item22")
        # item2.appendRow(item22)
        # model.appendRow(item1)
        # model.appendRow(item2)
        # cb.setModel(model)     #模型显示树形控件
        # cb.setView(QTreeView(cb))

        # cb.activated[str].connect(lambda val:print("条目被激活", val))
        # cb.currentIndexChanged[str].connect(lambda val:print("当前索引发生改变", val))
        # cb.currentTextChanged.connect(lambda val:print("当前文本发生改变", val))
        # cb.editTextChanged.connect(lambda val:print("当前编辑文本发生改变", val))
        # cb.highlighted[int].connect(lambda val:print("高亮发生改变", val))
        cb.highlighted[str].connect(lambda val:print("高亮发生改变", val))

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
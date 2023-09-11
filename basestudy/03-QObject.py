from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
        self.set_ui()
    def set_ui(self):
        # self.object_Test()
        # self.QObject对象名称和属性操作()
        # self.QOject父对象和子对象()
        # self.QObject信号槽()
        # self.QObject类型判定()
        self.QObject对象删除()

    def object_Test(self):
        #查找父类
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject对象名称和属性操作(self):
        #############测试API##############
        # obj=QObject()
        # obj.setObjectName("notice")
        # print(obj.objectName())
        #
        # obj.setProperty("test1","error")
        # obj.setProperty("test2","warning")
        # print(obj.property("test1"))
        ############测试API结束##############
        # print(obj.dynamicPropertyNames())
        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setObjectName("notice")
        label.setText("我是中国人")

        label2 = QLabel(self)
        label2.move(100,100)
        label2.setObjectName("notice")
        label2.setProperty("notice_level","normal")
        label2.setText("我是日本人")

    def QOject父对象和子对象(self):
        '''
        设置三个对象，结构图如下
                obj0
            obj1
        obj2
        '''

        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()

        obj1.setParent(obj0)
        obj2.setParent(obj1)

        obj2.setObjectName("oobbjj2")

        print(obj0.parent()) 
        #查找指定子对象
        print(obj0.findChild(QObject, "oobbjj2"))
        #查找所有子对象
        print(obj0.findChildren(QObject))

    def QObject信号槽(self):
        self.obj = QObject()
        # obj.destroyed
        # obj.objectNameChanged
        # def destroy_cao(obj):
        #     print("对象被释放了", obj)
        #
        # self.obj.destroyed.connect(destroy_cao)
        #
        # del self.obj
        def obj_name_cao(name):
            print("对象名称发生了改变", name)

        def obj_name_cao2(name):
            print("对象名称发生了改变2", name)

        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.objectNameChanged.connect(obj_name_cao2)

        # print(self.obj.receivers("objectNameChanged")) X
        print(self.obj.receivers(self.obj.objectNameChanged))
        self.obj.setObjectName("xxx")

        # self.obj.objectNameChanged.disconnect()
        # print(self.obj.signalsBlocked(), "1")
        # self.obj.blockSignals(True)
        # print(self.obj.signalsBlocked(), "2")
        # self.obj.setObjectName("ooo")
        #
        # self.obj.blockSignals(False)
        # print(self.obj.signalsBlocked(), "3")
        # # self.obj.objectNameChanged.connect(obj_name_cao)
        #
        # self.obj.setObjectName("xxoo")

        #*************信号与槽案例***************开始
        btn = QPushButton(self)
        btn.setText("点击我")
        def cao():
            print("点我嘎哈?")

        btn.clicked.connect(cao)


        #*************信号与槽案例***************结束

    def QObject类型判定(self):
        wiget = QWidget(self)
        label = QLabel(self)
        btn = QPushButton(self)

        print(label.isWidgetType())
        for i in self.children():
            print(i.inherits("QLabel"))
    def QObject对象删除(self):
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        self.obj1 = obj1
        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda : print("obj1对象被释放了"))
        obj2.destroyed.connect(lambda : print("obj2对象被释放了"))
        obj3.destroyed.connect(lambda : print("obj3对象被释放了"))

        #使用deleteLater不会马上被释放，当该对象调用完毕才会被释放
        obj2.deleteLater()
        print(obj1.children())

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
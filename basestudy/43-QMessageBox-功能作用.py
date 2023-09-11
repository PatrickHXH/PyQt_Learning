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
        # QMessageBox.aboutQt(self,"xx1")
        QMessageBox.about(self,"xx1","xx2")
        QMessageBox.question(self,"Xx1","xx2",QMessageBox.Ok | QMessageBox.Discard,QMessageBox.Discard)
        return None
        # 展示内容
        mb = QMessageBox(self)
        # mb.setModal(False)   #设置为非模态
        # mb = QMessageBox(QMessageBox.Warning,"XX1","XX2",QMessageBox.Ok | QMessageBox.Discard,self)
        # mb.setWindowModality(Qt.NonModal)  #设置为非模态
        mb.setTextInteractionFlags(Qt.TextEditorInteraction)
        mb.setWindowTitle("消息提示")
        mb.setIconPixmap(QPixmap("test.png").scaled(50, 50))
        mb.setTextFormat(Qt.PlainText)
        mb.setText("<h3>文件内容已经被修改</h3>")
        mb.setInformativeText("是否直接关闭，不保存？")
        mb.setCheckBox(QCheckBox("下次不再提醒",mb))
        mb.setDetailedText("<h4>你修改的内容是给每一行代码加了一个分号</h4>")

        #是否按钮
        # mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        #自定义按钮
        # mb.addButton(QPushButton("XX1",mb),QMessageBox.YesRole)
        # mb.addButton(QPushButton("XX2",mb),QMessageBox.NoRole)
        btn2 = mb.addButton("Xx2",QMessageBox.NoRole)
        #移除按钮
        # mb.removeButton(btn2)

        mb.setDefaultButton(btn2)
        mb.setEscapeButton(btn2)

        #信号
        mb.buttonClicked.connect(lambda btn:print(btn))
        mb.show()
        # mb.open()

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
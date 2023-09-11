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
        # result = QFileDialog.getOpenFileNames(self,"选择一个py","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")
        # result = QFileDialog.getOpenFileUrl(self, "选择一个文件",QUrl("./"),"All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")
        # result = QFileDialog.getSaveFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getExistingDirectory(self, "选择一个py文件", "./")
        # result = QFileDialog.getExistingDirectoryUrl(self, "选择一个py文件", QUrl("./"))
        # print(result)

        def test():
            fd = QFileDialog(self,"选择一个文件","../","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")
            fd.fileSelected.connect(lambda file:print(file))
            # fd.setAcceptMode(QFileDialog.AcceptSave)  #变为保存按钮
            # fd.setDefaultSuffix("txt")  #选择默认后缀
            # fd.setFileMode(QFileDialog.Directory)  #选择文件
            # fd.setNameFilter("IMG(*.jpg *.png *.jpeg")
            # fd.setNameFilters(["All(*.*)","Images(*.png *.jpg)","Python文件(*.py)"])
            # fd.setViewMode(QFileDialog.Detail)
            fd.setLabelText(QFileDialog.FileName,"胖哥的文件")
            fd.setLabelText(QFileDialog.Accept,"胖哥的接受")
            fd.setLabelText(QFileDialog.Reject,"胖哥的拒绝")

            # fd.currentChanged.connect(lambda path:print("当前路径发生改变时：",path))
            # fd.currentUrlChanged.connect(lambda url:print("当前Qurl发生改变时：",url))
            # fd.directoryEntered.connect(lambda url:print("当前目录字符串进入时：",url))
            # fd.directoryUrlEntered.connect(lambda url:print("当前Qurl发生改变时：",url))
            # fd.filterSelected.connect(lambda filter:print("当选择后缀名称改变时：",filter))
            fd.setFileMode(QFileDialog.ExistingFiles)
            fd.fileSelected.connect(lambda val: print("单个文件被选中-字符串", val))
            fd.filesSelected.connect(lambda val: print("多个文件被选中-列表[字符串]", val))
            fd.urlSelected.connect(lambda val: print("单个文件被选中-url", val))
            fd.urlsSelected.connect(lambda val: print("多个文件被选中-列表[url]", val))

            fd.open()

        btn  =QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100,100)
        btn.clicked.connect(test)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
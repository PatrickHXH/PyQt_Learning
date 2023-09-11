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
        # self.setStyleSheet("background-color:red")
        # QColorDialog.setCustomColor(0,QColor(10,20,100))
        # QColorDialog.setStandardColor(2, QColor(255, 0, 0))
        # cd = QColorDialog(QColor(100, 200, 150),self)
        # cd.setWindowTitle("选择一个好看的颜色")
        #
        # def color():
        #     palette = QPalette()
        #     # palette.setColor(QPalette.Background,col)
        #     palette.setColor(QPalette.Background,cd.currentColor())
        #     self.setPalette(palette)
        # # cd.colorSelected.connect(color)  #点确定后打印
        # cd.currentColorChanged.connect(color)
        # cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        # cd.show()

        btn =QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(cd.customCount()))
        # btn.clicked.connect(lambda :print(QColorDialog.customCount()))

        def test():
            cd = QColorDialog(self)
            cd.setOptions(QColorDialog.NoButtons)
            cd.setWindowTitle("选择一个人生的颜色")
            def sel_color(color):
                palette = QPalette()
                palette.setColor(QPalette.ButtonText,color)
                self.setPalette(palette)
            # cd.colorSelected.connect(sel_color)
            cd.currentColorChanged.connect(sel_color)
            cd.show()

            # color = QColorDialog.getColor(QColor(10,20 ,100),self,"选择颜色")
            # print(color)
            # #设置调色板
            # palette = QPalette()
            # # palette.setColor(QPalette.Background,col)
            # palette.setColor(QPalette.Background,color)
            # self.setPalette(palette)

        btn.clicked.connect(test)



if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
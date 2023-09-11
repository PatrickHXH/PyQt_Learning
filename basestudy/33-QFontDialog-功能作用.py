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
        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        # fd = QFontDialog(font,self)
        # fd.setOption(QFontDialog.NoButtons)   #没有按钮
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)   #没有按钮
        # print(fd.testOption(QFontDialog.MonospacedFonts))  #查看有没有生效

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100,100)

        # def font_sel():
        #     print("字体已经被选择", fd.selectedFont().family())
        # btn.clicked.connect(lambda: fd.open(font_sel))  #打开字体窗口方法一

        # fd.show()

        label = QLabel(self)
        label.move(300,300)
        label.setText("社会顺哥")

        # def cfc(font):
        #     label.setFont(font)
        #     label.adjustSize()
        # fd.currentFontChanged.connect(cfc)


        def font_sel():                                            #打开字体窗口方法二
            # print("字体已被选择",fd.selectedFont().family())
            result = QFontDialog.getFont(font,self,"选择一个好看的字体")
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()
        btn.clicked.connect(font_sel)

        # print(fd.exec())
        # if fd.exec():
        #     print("字体已经被选择", fd.selectedFont().family())


if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
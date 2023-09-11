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
        label = QLabel("社会我黄哥",self)
        # label = QLabel("账号(&s)：",self)
        label = QLabel("<a href ='www.baidu.com'>百度</a>",self)
        label.setStyleSheet("background-color:red")
        label.move(100,100)
        label.resize(150,300)
        # label.adjustSize()

        # label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        label.setIndent(20)

        # label.setTextFormat(Qt.PlainText)
        le1 =QLineEdit(self)
        le1.move(250,250)

        le2 = QLineEdit(self)
        le2.move(250,300)

        label.setBuddy(le1)
        # label.setPixmap(QPixmap("test.png"))
        # label.adjustSize()
        label.setScaledContents(True)

        # label.setTextInteractionFlags(Qt.TextSelectableByMouse)  #可被选中
        label.setOpenExternalLinks(True) #打开外部链接
        label.setWordWrap(True)  #超出宽度换行，并保持单词完整性
        label.setSelection(1,2)

        # pic = QPicture()
        # painter = QPainter(pic)
        # painter.setBrush(QBrush(QColor(100,200,100)))
        # painter.drawEllipse(0,0,200,200)
        # label.setPicture(pic)

        movie = QMovie("test.png")
        label.setMovie(movie)
        movie.start()
        movie.setSpeed(200)
        label.clear()

        #信号监听
        label.linkHovered.connect()   #鼠标放置链接上的监听
        label.linkActivated.connect()
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
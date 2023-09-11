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
        red_btn = QPushButton("红色按钮",self)
        green_btn = QPushButton("绿色按钮",self)
        red_btn.resize(100,100)
        green_btn.resize(100,100)
        red_btn.setStyleSheet("""
            background-color:red;
        """)
        green_btn.setStyleSheet("""
            background-color:green;
        """)
        #动画设置
        animation = QPropertyAnimation(red_btn,b"pos",self)
        animation.setKeyValueAt(0,QPoint(150,150))
        animation.setKeyValueAt(0.25,QPoint(550,150))
        animation.setKeyValueAt(0.5,QPoint(550,550))
        animation.setKeyValueAt(.75,QPoint(150,550))
        animation.setKeyValueAt(1,QPoint(150,150))

        animation.setDuration(2000)
        # animation.start()

        animation2 = QPropertyAnimation(green_btn,b"pos",self)
        animation2.setKeyValueAt(0,QPoint(0,0))
        animation2.setKeyValueAt(0.25,QPoint(0,700))
        animation2.setKeyValueAt(0.5,QPoint(700,700))
        animation2.setKeyValueAt(.75,QPoint(700,0))
        animation2.setKeyValueAt(1,QPoint(0,0))

        animation2.setDuration(2000)
        # animation2.start()

        animation_group1 = QSequentialAnimationGroup(self)
        animation_group1.addAnimation(animation)

        # animation_group1.addPause(5000)
        pasuse_animation = QPauseAnimation()
        pasuse_animation.setDuration(5000)
        animation_group1.addAnimation(pasuse_animation)

        animation_group1.addAnimation(animation2)
        animation_group1.start()

        red_btn.clicked.connect(animation_group1.pause)
        green_btn.clicked.connect(animation_group1.resume)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
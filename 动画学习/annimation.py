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
        btn = QPushButton("测试按钮",self)
        btn.move(100,100)
        btn.resize(200,200)
        btn.setStyleSheet("background-color:cyan")

        # 1、创建一个动画对象，并且设置目标属性
        # animation = QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b"size")
        animation = QPropertyAnimation(btn,b"pos",self)
        # animation = QPropertyAnimation(btn,b"size",self)
        # animation = QPropertyAnimation(btn,b"geometry",self)
        # animation = QPropertyAnimation(self,b"windowOpacity",self)

        #2、设置属性值 开始 插值 结束
        animation.setStartValue(QPoint(0,0))
        animation.setEndValue(QPoint(300,300))
        # animation.setStartValue(QSize(0,0))
        # animation.setEndValue(QSize(300,300))
        # animation.setStartValue(QRect(0, 0, 100, 100))
        # animation.setEndValue(QRect(200,200,300,300))
        # animation.setStartValue(1)
        # animation.setKeyValueAt(0.5,0.5)
        # animation.setEndValue(1)

        #3、动画时长
        animation.setDuration(3000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.setLoopCount(3)
        animation.setDirection(QAbstractAnimation.Backward)
        #4、启动动画
        animation.start()
        print(animation.totalDuration(),animation.duration())
        # btn.clicked.connect(lambda :print(animation.loopCount(),animation.currentLoop()))
        # btn.clicked.connect(lambda :print(animation.currentTime(),animation.currentLoopTime()))

        def animation_operation():
            if animation.state() == QAbstractAnimation.Running:
                animation.pause()
            elif animation.state() == QAbstractAnimation.Paused:
                animation.resume()
        btn.clicked.connect(animation_operation)
        animation.currentLoopChanged.connect(lambda val:print("当前循环次数发生改变",val))
        animation.finished.connect(lambda :print("动画执行完毕"))
        animation.stateChanged.connect(lambda ns,os:print("状态发生改变",ns,os))

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
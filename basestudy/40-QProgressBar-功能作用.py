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
        pb = QProgressBar(self)
        pb.resize(400,40)
        print(pb.minimum())
        print(pb.maximum())

        pb.setMinimum(0)
        pb.setMaximum(80)
        pb.setValue(20)
        # pb.setRange(0,0)
        pb.setFormat(f"当前人数{pb.value() - pb.minimum()} / 总人数 %m")

        btn = QPushButton(self)
        btn.move(200,200)
        btn.setText("测试按钮")
        def test():
            # pb.reset()
            # print(pb.minimum())
            # print(pb.maximum())
            # print(pb.value())
            # pb.resetFormat()
            # pb.setAlignment(Qt.AlignCenter)

            print(pb.text())
            pb.setOrientation(Qt.Vertical)
            pb.resize(40,400)
            print(pb.isTextVisible())
            pb.setTextDirection(QProgressBar.TopToBottom)
            pb.setInvertedAppearance(True)
        btn.clicked.connect(test)

        timer = QTimer(pb)
        def change_progess():
            if pb.value() == pb.maximum():
                timer.stop()
            pb.setValue(pb.value() + 1)
        timer.timeout.connect(change_progess)
        timer.start(1000)
        pb.valueChanged.connect(lambda val:print("当前进度值为：",val))
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
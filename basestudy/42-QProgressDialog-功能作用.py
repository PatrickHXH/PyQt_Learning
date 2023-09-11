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
        pd = QProgressDialog("xxx1","xxx2",1,1000,self)
        # pd.open(lambda :print("对话框被取消"))
        # pd.setAutoClose(False)  #不要自动关闭
        # pd.setAutoReset(False)
        pd.setWindowTitle("xxx3")
        pd.setLabelText("下载进度")
        pd.setCancelButtonText("取消下载")
        pd.setRange(0,100)
        pd.setValue(95)
        print(pd.minimum())
        print(pd.maximum())
        pd.setAutoReset(False)
        pd.show()
        # pd.setMinimumDuration(0)
        # pd.setValue(50)
        timer = QTimer(pd)
        def test():
            print(pd.value())
            if pd.value() >= pd.maximum() or pd.wasCanceled():
                timer.stop()
            else:
                pd.setValue(pd.value() + 1)
            if pd.value() == 98:
                pd.cancel()
        timer.timeout.connect(test)
        timer.start(1000)

        pd.canceled.connect(timer.stop)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
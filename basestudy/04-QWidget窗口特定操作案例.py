import sys
from PyQt5.Qt import *




class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # window.setWindowOpacity(0.8)
        self.resize(500,500)
        #公共数据
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 40
        self.setup_ui()
    def setup_ui(self):

        # 关闭按钮
        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)

        # 最大化按钮
        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)


        # 最小化按钮
        min_btn = QPushButton(self)
        self.min_btn = min_btn
        min_btn.setText("最小化")
        min_btn.resize(self.btn_w, self.btn_h)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText("窗口")

        # 按钮事件
        close_btn.pressed.connect(self.close)
        min_btn.pressed.connect(self.showMinimized)
        max_btn.pressed.connect(max_normal)

    def resizeEvent(self, evt):
        print("窗口大小发生了变化")
        window_w = self.width()
        close_btn_x = window_w -self. btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

app =QApplication(sys.argv)

#设定按钮宽高、上边距

window = Window()
#添加三个子控件 - 窗口的右上角



window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作

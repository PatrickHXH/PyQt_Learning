from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        self.move_flag = False
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(500,500)

    def set_ui(self):
        # 展示内容
        pass
    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
            #获取窗口原始坐标点，获取鼠标相当于桌面的坐标点
            self.origin_x = self.x()
            self.origin_y = self.y()

            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

    def mouseMoveEvent(self, evt):
        if self.move_flag:
            self.move_x = evt.globalX() - self.mouse_x
            self.move_y = evt.globalY() - self.mouse_y
            #移动位置
            dest_x = self.origin_x + self.move_x
            dest_y = self.origin_y + self.move_y
            self.move(dest_x,dest_y)

    def mouseReleaseEvent(self, evt):
        self.move_flag = False

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.setMouseTracking(True)
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
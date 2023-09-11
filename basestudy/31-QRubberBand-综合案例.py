from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
        self.set_ui()
    def set_ui(self):
        # 添加子控件
        for i in range(0,30):
            cb = QCheckBox(self)
            cb.setText(f"{i}")
            cb.move(i%4*80,i//4 *60)
        self.rb = QRubberBand(QRubberBand.Rectangle, self)
    def mousePressEvent(self, evt):
        #创建橡皮筋选中控件
        self.origin_pos = evt.pos()
        self.rb.setGeometry(QRect(self.origin_pos,QSize()))
        self.rb.show()

    def mouseMoveEvent(self, evt):
        self.rb.setGeometry(QRect(self.origin_pos, evt.pos()).normalized())
    def mouseReleaseEvent(self, evt):
        # 1. 获取橡皮筋控件的尺寸范围
        rect = self.rb.geometry()
        # 2. 遍历所有的子控件, 查看, 哪些子控件在区域范围
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):
                print(child)
                child.toggle()
        self.rb.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
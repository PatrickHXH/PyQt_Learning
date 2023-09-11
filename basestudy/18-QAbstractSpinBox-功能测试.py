from PyQt5.Qt import *
import sys
class MyAsb(QAbstractSpinBox):
    def __init__(self,parent=None,num="0",*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.lineEdit().setText(num)
    def stepEnabled(self):
        #0 --9
        # current_num = int(self.text())
        # if current_num == 0:
        #     return QAbstractSpinBox.StepUpEnabled
        # elif current_num ==9:
        #     return  QAbstractSpinBox.StepDownEnabled
        # elif current_num <0 or current_num > 9:
        #     return QAbstractSpinBox.StepNone
        # else:
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        current_num = int(self.text())+p_int
        self.lineEdit().setText(str(current_num))

    def validate(self, p_str, p_int):
        # 18 - 180
        num = int(p_str)
        if num < 18:
            return (QValidator.Intermediate, p_str, p_int)
        elif num <= 180:
            return (QValidator.Acceptable, p_str, p_int)
        else:
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, p_str):
        print(p_str)
        return "18"
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def btn_test(self):
        print(self.asb.lineEdit().setText("88"))
        cl = QCompleter(["sz","123","18"],self.asb)
        self.asb.lineEdit().setCompleter(cl)
        self.asb.lineEdit().setAlignment(Qt.AlignCenter)

        # self.asb.setAlignment(Qt.AlignCenter)

        # print(self.asb.hasFrame())
        # self.asb.setFrame(False)

        # self.asb.clear()
        self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)
    def set_ui(self):
        # 展示内容
        asb =MyAsb(self)
        self.asb = asb
        asb.resize(100,30)
        asb.move(100,100)
        asb.setAccelerated(True)

        test_btn = QPushButton(self)
        test_btn.move(200,200)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

        self.asb.editingFinished.connect(lambda :print("结束编辑"))
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
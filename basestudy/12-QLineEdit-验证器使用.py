from PyQt5.Qt import *
import sys
#自定义验证器子类
class AgeValidator(QValidator):
    def validate(self, input_str,pos_int):
        print("xxx：",input_str)
        #判定结果字符串，应该全部都是由一些数字组成
        try:
            if 18<=int(input_str)<=180:
                return (QValidator.Acceptable, input_str, pos_int)
            elif 1<=int(input_str)<=17:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)
        except:
            #如果删除后，则返回中间状态
            if len(input_str) ==0:
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)
    #验证器中间会进入fixup方法，修补后再次调用validate验证，只会修复一次
    def fixup(self, p_str):
        print("再次判定",p_str)
        try:
            if int(p_str) < 18:
                return "18"
            return "180"
        except:
            return "18"

#二次定义系统验证器子类
class MyAgeValidator(QIntValidator):
    def fixup(self, p_str):
        print("xxxx",p_str)
        if len(p_str) == 0 or int(p_str)<18:
            return "18"

class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)

    def set_ui(self):
        # 展示内容
        le = QLineEdit(self)
        le.move(100,100)
        # validator = AgeValidator()  #使用自定义验证器子类
        validator = MyAgeValidator(18,180)  #使用系统提供的验证器子类          QDoubleValidator
        le.setValidator(validator)

        le2 = QLineEdit(self)
        le2.move(200,200)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
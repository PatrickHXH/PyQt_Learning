from PyQt5.Qt import *
import sys
from resource.caculator import Ui_Form

class Caculator(QObject):
    show_content = pyqtSignal(str)
    def __init__(self,parent):
        super().__init__(parent)
        self.key_models=[]
    def caculate(self):
        if len(self.key_models) >0 and self.key_models[-1]["role"] =="operator":
            self.key_models.pop(-1)
        expression = ""
        for model in self.key_models:
            expression += model["title"]
        result = eval(expression)
        print(result)
        return result

    def parse_key_model(self,key_model):
        print(key_model)
        if key_model["role"] == "clear":
            print("清空所有内容")
            self.show_content.emit("0.0")
            self.key_models = []
            return None
        if  key_model["role"] == "equal":
            print("计算所有内容")
            result = self.caculate()
            self.show_content.emit(str(result))
            return None

        #如果列表长度为0
        if len(self.key_models) == 0:
            #如果当前点击为数字
            if key_model["role"] == "num":
                if key_model["title"] ==".":
                    key_model["title"] ="0."
                self.key_models.append(key_model)
                self.show_content.emit(self.key_models[-1]["title"])
            return None
        print(self.key_models)

        if key_model["title"] in ("%","+/-"):
            if self.key_models[-1]["role"] !="num":
                return None
            else:
                if key_model["title"] == "%":
                    self.key_models[-1]["title"] = str(float(self.key_models[-1]["title"]) / 100)
                elif key_model["title"] =="+/-":
                    self.key_models[-1]["title"] = str(float(self.key_models[-1]["title"]) * -1)
                self.show_content.emit(self.key_models[-1]["title"])
            return None

        #两个角色若相等，则进行判定是拼接还是替换，否则直接追加
        if key_model["role"] == self.key_models[-1]["role"]:
            #前后点击为数字则拼接
            if key_model["role"] == "num":
                #判断列表最后数字是否含小数点
                if key_model["title"] =="." and self.key_models[-1]["title"].__contains__("."):
                    return None
                #判断列表最后数字不为0
                if self.key_models[-1]["title"] != "0":
                    self.key_models[-1]["title"] += key_model["title"]
                #若列表最后一个为0
                else:
                    self.key_models[-1]["title"] =key_model["title"]
                self.show_content.emit(self.key_models[-1]["title"])
            #前后为运算符则替代
            if key_model["role"] == "operator":
                self.key_models[-1]["title"] = key_model["title"]
                self.show_content.emit(str(self.caculate()))
        else:
            if key_model["title"] in (".","%","+/-"):
                return None
            if key_model["role"] == "num":
                self.show_content.emit(key_model["title"])
            elif key_model["role"] == "operator":
                self.show_content.emit(str(self.caculate()))
            self.key_models.append(key_model)
        print(self.key_models)
class CaculatorPane(QWidget,Ui_Form):

    def __init__(self,parent=None,*args,**Kwargs):
        #继承Qwidget
        super().__init__(parent,*args,**Kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)  #设置样式
        self.caculator = Caculator(self)
        self.caculator.show_content.connect(self.show_content)
    def show_content(self,content):
        self.lineEdit.setText(content)
    def get_key(self,title,role):
        self.caculator.parse_key_model({"title":title,"role":role})

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = CaculatorPane()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
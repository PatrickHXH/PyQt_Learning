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
        # result = QInputDialog.getInt(self,"xxx1","xxxx2")
        # result = QInputDialog.getDouble(self,"xxx1","xxxx2",888,88,decimals=2)
        # result = QInputDialog.getText(self,"xxx1","xxxx2",echo=QLineEdit.Password)
        # result = QInputDialog.getMultiLineText(self,"xxx1","xxxx2","default")
        # result = QInputDialog.getItem(self,"xxx1","xxxx2",["1","2","3"],2)
        # print(result)

        input_d = QInputDialog(self,Qt.FramelessWindowHint)
        input_d.setOption(QInputDialog.UseListViewForComboBoxItems)
        input_d.setLabelText("请输入您的姓名")
        input_d.setOkButtonText("好的")
        input_d.setCancelButtonText("我想取消")
        # input_d.setComboBoxItems(["1","2","3"])

        input_d.setInputMode(QInputDialog.IntInput)
        # input_d.setInputMode(QInputDialog.TextInput)
        # input_d.setDoubleRange(9.9,19.9)
        # input_d.setDoubleStep(2)
        # input_d.setDoubleDecimals(3)

        input_d.setComboBoxItems(["abc","def","ccc"])
        # input_d.setComboBoxEditable(True)

        #信号
        input_d.intValueChanged.connect(lambda val:print("整型数据发生改变：",val))
        input_d.intValueSelected.connect(lambda val:print("整型数据最终被选中：",val))
        input_d.doubleValueChanged.connect(lambda val:print("浮点数据发生改变：",val))
        input_d.doubleValueSelected.connect(lambda val:print("浮点数据最终被选中：",val))
        input_d.textValueChanged.connect()
        input_d.textValueSelected.connect()
        input_d.show()
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
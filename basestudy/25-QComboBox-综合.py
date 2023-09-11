from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
        self.city_dic = {
            "北京": {
                "东城": "001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            }
        }
        self.set_ui()
    def set_ui(self):
        # 展示内容
        #创建两个下拉列表控件
        pro = QComboBox(self)
        city = QComboBox(self)
        self.pro = pro
        self.city = city
        pro.move(100,100)
        city.move(250,100)

        #监听省下拉列表值发生改变
        pro.currentIndexChanged[str].connect(self.pro_changed)
        # self.pro_changed(pro.currentText())


        #监听城市下拉列表值发生改变
        # city.currentIndexChanged[str].connect(self.city_changed)
        city.currentIndexChanged[int].connect(self.city_changed)
        # self.city_changed(city.currentIndex())

        #展示数据到第一个下拉选择控件当中
        pro.addItems(self.city_dic.keys())

    def pro_changed(self,pro_name):
        print(pro_name)
        #根据省的名称到字典里面获取城市
        citys = self.city_dic[pro_name]
        self.city.blockSignals(True)
        self.city.clear()
        self.city.blockSignals(False)
        # self.city.addItems(citys.keys())
        for key,value in citys.items():
            self.city.addItem(key,value)

    def city_changed(self,item_idx):
        print(item_idx)
        print(self.city.itemData(item_idx))

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    # window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
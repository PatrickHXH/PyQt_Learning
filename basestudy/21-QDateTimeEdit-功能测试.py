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
        # dt = QDateTime(2018,12,12,12,30)
        # dt = QDateTime.currentDateTime()
        # dt = dt.addYears(-2)
        # QDateTimeEdit(dt,self)

        dte = QDateTimeEdit(self)
        # dte = QDateTimeEdit(QDateTime.currentDateTime(), self)
        # dte = QDateTimeEdit(QDate.currentDate(), self)
        # dte = QDateTimeEdit(QTime.currentTime(), self)
        dte.move(100,100)
        dte.setDisplayFormat("yy-MM-dd $ m: ss: zzz")

        # print(dte.sectionCount())

        # time = QTime.currentTime()
        # time.start()
        btn = QPushButton(self)
        btn.move(200,200)
        btn.setText("测试")
        # btn.clicked.connect(lambda :print(time.elapsed() / 1000))
        def test():
            #选择某个节点的光标
            # dte.setCurrentSection(QDateTimeEdit.DaySection)
            # print(dte.sectionText(QDateTimeEdit.DaySection))

            # dte.setMaximumDateTime(QDateTime(2020, 8, 15, 12, 30))
            # dte.setMinimumDateTime(QDateTime.currentDateTime().addDays(-3))

            # dte.setCalendarPopup(True)
            print(dte.date())
            print(dte.time())
        # btn.clicked.connect(lambda :print(dte.currentSectionIndex()))
        btn.clicked.connect(test)
        #信号
        dte.dateTimeChanged.connect(lambda val:print(val))
        dte.dateChanged.connect(lambda val:print("日期发生改变:",val))
        dte.timeChanged.connect(lambda val:print("时间发生改变:",val))

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
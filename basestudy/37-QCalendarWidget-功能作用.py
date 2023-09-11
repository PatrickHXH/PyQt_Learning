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
        cw = QCalendarWidget(self)
        #设置日期范围
        cw.setMinimumDate(QDate(1990,1,1))
        cw.setMaximumDate(QDate(2023,8,31))
        # cw.setDateRange()
        cw.setSelectedDate(QDate(-9999,1,1))
        #不可使用键盘
        # cw.setDateEditEnabled(False)
        #接受延迟，3000毫秒
        cw.setDateEditAcceptDelay(3000)

        btn = QPushButton(self)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(cw.monthShown()))
        # btn.clicked.connect(lambda :print(cw.yearShown()))
        # btn.clicked.connect(lambda :print(cw.selectedDate()))
        btn.move(500,500)

        # btn.clicked.connect(cw.showToday)
        # btn.clicked.connect(cw.showSelectedDate)
        # btn.clicked.connect(cw.showNextYear)
        btn.clicked.connect(cw.showNextMonth)
        btn.clicked.connect(lambda :cw.setCurrentPage(2008,8))
        # cw.setNavigationBarVisible(False) #dao导航条隐藏

        cw.activated.connect(lambda data:print(data))
        cw.selectionChanged.connect(lambda :print("选中日期发生改变：",cw.selectedDate()))
        cw.setSelectedDate(QDate(2008,8,8))  #设置默认值

        cw.setFirstDayOfWeek(Qt.Sunday)
        cw.setGridVisible(True)  #设置网格


        tcf = QTextCharFormat()
        tcf.setFontPointSize(16)
        tcf.setFontUnderline(True)

        cw.setHeaderTextFormat(tcf)  #设置文字格式

        cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)  #星期日在前
        # cw.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)  #行去掉

        cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader) #列去掉

        t_tcf =  QTextCharFormat()
        t_tcf.setFontPointSize(20)
        t_tcf.setToolTip("这是星期二")
        cw.setWeekdayTextFormat(Qt.Tuesday,tcf)

        cw.setDateTextFormat(QDate(2018,12,12),t_tcf)

        # cw.setSelectionMode(QCalendarWidget.NoSelection)  #不能被选中
        # cw.setSelectedDate(QDate(2023,8,1))
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
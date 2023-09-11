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
        name_label = QLabel("姓名:")
        age_label = QLabel("年龄:")
        name_le = QLineEdit()
        age_sb = QSpinBox()

        sex_label = QLabel("性别")
        male_rb  =QRadioButton("男")
        female_rb =QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn = QPushButton("提交按钮")
        #创建布局管理器
        layout = QFormLayout()

        #把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        #把需要布局的子控件交给布局管理器进行布局
        # layout.addWidget(name_label)
        # layout.addWidget(name_le)


        layout.addRow(name_label,name_le)
        layout.addRow(age_label,age_sb)
        # layout.addRow("姓名(&n):",name_le)
        layout.addRow(sex_label,h_layout)
        # layout.addRow("年龄(&g):",age_sb)
        layout.addRow(submit_btn)
        # layout.insertRow(1, "性别:", h_layout)
        #
        # print(layout.rowCount())
        # print(layout.getWidgetPosition(name_label))
        # print(layout.getLayoutPosition(h_layout))

        # layout.setWidget(0,QFormLayout.LabelRole,name_label)
        # layout.setWidget(0,QFormLayout.FieldRole,name_le)
        # layout.addRow(name_label)
        # layout.setWidget(0,QFormLayout.LabelRole,sex_label)
        # layout.setWidget(0,QFormLayout.LabelRole,name_le)

        # age_sb.destroyed.connect(lambda :print("年龄步长被释放"))
        # age_label.destroyed.connect(lambda :print("年龄标签被释放"))
        # layout.removeRow(age_label)    #移除一整行
        # layout.removeWidget(age_label)   #移除一部分控件
        # layout.removeRow(1)
        # layout.takeRow(1)
        # age_sb.hide()x
        # age_label.hide()

        print(layout.labelForField(name_le).setText("xxxxxxxxxxxxxxxxxxxxxxxx"))  #修改标签名字
        # layout.setRowWrapPolicy(QFormLayout.WrapAllRows)  #上下布局
        layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.setLabelAlignment(Qt.AlignRight)
        layout.setVerticalSpacing(60)   #垂直间距
        layout.setHorizontalSpacing(20)  #水平间距
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
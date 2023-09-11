import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(500,500)

rb_nan = QRadioButton("男",window)
rb_nan.move(10,50)
rb_nv = QRadioButton("女",window)
rb_nv.move(10,100)
#创建组按钮
sex_group = QButtonGroup(window)
#设置ID—第一种方法
sex_group.addButton(rb_nan,1)
sex_group.addButton(rb_nv,2)
#设置ID—第二种方法
rb_nan.setChecked(True)
sex_group.setId(rb_nan,1)
print(sex_group.checkedId())
print(sex_group.id(rb_nan))

#按钮组移除按钮
# sex_group.removeButton(rb_nv)
#按钮设置互斥关系
# sex_group.setExclusive(False)

#组按钮信号
def test(val):
    print(sex_group.id(val))
# sex_group.buttonToggled.connect(test)
# sex_group.buttonClicked[int].connect(test)
sex_group.buttonClicked.connect(test)


rb_yes = QRadioButton("Yes",window)
rb_yes.move(100,50)
rb_no = QRadioButton("No",window)
rb_no.move(100,100)
answer_group = QButtonGroup(window)
answer_group.addButton(rb_yes,1)
answer_group.addButton(rb_no,2)


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




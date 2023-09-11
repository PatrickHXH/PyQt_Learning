import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)
window = QWidget()
window.resize(1500,1500)

le = QLineEdit(window)
le.move(500,500)
le.resize(500,500)
#设置文字间距和光标位置
le.setTextMargins(0,0,50,50)
le.setAlignment(Qt.AlignLeft | Qt.AlignTop)

#拖拽
le.setDragEnabled(True)

btn = QPushButton(window)
btn.setText("按钮")
btn.move(100,200)

le.textEdited.connect(lambda val: print("文本框编辑的时候", val))
le.textChanged.connect(lambda val: print("文本框内容发生改变", val))

# le.returnPressed.connect(lambda :print("回车键被按下"))
# le.returnPressed.connect(lambda :le2.setFocus())
# le.editingFinished.connect(lambda :print("结束编辑"))

def cursor_move():
    #True为选中，False为不选中
    #向右移动并选中
    # le.cursorForward(True,3)

    #从光标向左选中，遇到空格停止
    # le.cursorWordBackward(True)

    # 从光标向左选中，遇到空格不停止
    # le.home(True)

    #移动光标至中间
    # le.setCursorPosition(len(le.text())//2)

    #打印光标至第x位置
    # print(le.cursorPosition())

    #根据坐标打印光标的位置
    # print(le.cursorPositionAt(QAction(15, 5)))
    # le.setFocus()
    le.cursorBackward(True,2)
    le.backspace()
    le.setFocus()

btn.clicked.connect(cursor_move)


window.show()
sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




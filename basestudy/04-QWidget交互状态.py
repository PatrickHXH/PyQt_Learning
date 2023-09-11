import sys
from PyQt5.Qt import *


app =QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

class Btn(QPushButton):
    def paintEvent(self, evt):
        return super().paintEvent(evt)
'''
#点击后按钮被隐藏

btn = Btn(window)
btn.setText("按钮")
btn.pressed.connect(lambda :btn.setVisible(False))

# btn.setEnabled(False)
#*号默认隐藏，被编辑的状态会显示
window.setWindowTitle("交互状态[*]")
window.setWindowModified(True)
print(window.isWindowModified())
'''
# window.setVisible(True)

#测试隐藏控件后没有被释放
btn = Btn(window)
btn.setText("按钮")
btn.destroyed.connect(lambda :print("按钮被释放了"))

# btn.setVisible(False)
#程序运行完，按钮才被释放
# btn.deleteLater()
#按钮马上被释放
btn.setAttribute(Qt.WA_DeleteOnClose,True)
btn.close()
window.show()


sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作




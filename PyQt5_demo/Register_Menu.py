from PyQt5.Qt import *
import sys
from resource.register import Ui_Form
class RegisterPane(QWidget,Ui_Form):
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str,str)
    def __init__(self,parent=None,*args,**Kwargs):
        #继承Qwidget
        super().__init__(parent,*args,**Kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)  #设置样式
        self.animation_targets = [self.about_menue_btn,self.reset_menue_btn,self.exit_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

    def show_hide_menue(self,checked):
        print("显示和隐藏")
        animation_group = QSequentialAnimationGroup(self)  # 创建动画组
        for idx,target in enumerate(self.animation_targets):
            animation = QPropertyAnimation(target,b"pos",self)  #创建动画对象
            if not checked:
                animation.setStartValue(self.main_menue_btn.pos())
                animation.setEndValue(self.animation_targets_pos[idx])
            else:
                animation.setStartValue(self.animation_targets_pos[idx])
                animation.setEndValue(self.main_menue_btn.pos())
            animation.setDuration(300)
            animation.setEasingCurve(QEasingCurve.InOutBounce)  #设置弹性动画
            animation_group.addAnimation(animation)  #动画组添加动画对象
        animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)
    def about_menue(self):
        print("关于")
        QMessageBox.about(self,"百度","www.baidu.com")

    def reset_menue(self):
        print("重置")
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()

    def exit_menue(self):
        print("退出")
        self.exit_signal.emit()

    def check_register(self):
        print("注册")
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        self.register_account_pwd_signal.emit(account_txt,password_txt)

    def enable_register(self):
        print("判定")
        account_text = self.account_le.text()
        password_txt = self.password_le.text()
        cp_text = self.confirm_pwd_le.text()
        if len(account_text) >0 and len(password_txt) >0 and len(cp_text) >0 and password_txt == cp_text:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = RegisterPane()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
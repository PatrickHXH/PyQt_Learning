from Login_Menu import LoginPane
from Register_Menu import RegisterPane
from Caculator_Pane import CaculatorPane
from PyQt5.Qt import *
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    login_pane = LoginPane()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()
    CaculatorPane = CaculatorPane()
    #函数
    def exit_register_pane():
        animation = QPropertyAnimation(register_pane,b"pos",login_pane)
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InOutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def show_register_pane():
        animation = QPropertyAnimation(register_pane,b"pos",login_pane)
        animation.setStartValue(QPoint(0,login_pane.height()))
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def check_login(account,pwd):
        if account=="123124" and pwd=="456":
            print("登录成功")
            CaculatorPane.show()
            login_pane.hide()
        else:
            login_pane.show_error_animation()

   #信号连接
    register_pane.exit_signal.connect(exit_register_pane)
    register_pane.register_account_pwd_signal.connect(lambda account,pwd:print(account,pwd))
    login_pane.show_register_pane_signal.connect(show_register_pane)
    login_pane.check_login_signal.connect(check_login)
    login_pane.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
from PyQt5.Qt import *
import sys
from resource.login import Ui_Form
class LoginPane(QWidget,Ui_Form):
    show_register_pane_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)
    def __init__(self,parent=None,*args,**Kwargs):
        #继承Qwidget
        super().__init__(parent,*args,**Kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)  #设置样式
        movie = QMovie(":/login/images/login_top_bg.jpg")
        movie.setScaledSize(QSize(500,232))
        self.login_top_bg_label.setMovie(movie)
        movie.start()
    def show_register_pane(self):
        self.show_register_pane_signal.emit()
    def open_qq_link(self):
        link = "https://qm.qq.com/cgi-bin/qm/qr?k=gNcj0nKnCPIfhnRerldDcbFJAJeGyoH3&jump_from=webapi&authKey=ba6zeJdutQkq0BZ5DXYIRd2Gm6kK7H8GfM8vaa/R4M+hMc5XBRc5WZU+BV9q3TZc"
        QDesktopServices.openUrl(QUrl(link))
    def enable_login_btn(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        if len(account) >0 and len(pwd) >0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)
    def check_login(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.check_login_signal.emit(account,pwd)

    def auto_login(self,checked):
        if checked:
            self.remember_pwd_cb.setChecked(True)
    def remember_pwd(self,checked):
        if not checked:
            self.auto_login_cb.setChecked(False)
    def show_error_animation(self):
        animation = QPropertyAnimation(self.login_bottom,b"pos",self)
        animation.setKeyValueAt(0,self.login_bottom.pos())
        animation.setKeyValueAt(0.2,self.login_bottom.pos()+QPoint(15,0))
        animation.setKeyValueAt(0.5,self.login_bottom.pos())
        animation.setKeyValueAt(0.7,self.login_bottom.pos()+QPoint(-15,0))
        animation.setKeyValueAt(1,self.login_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = LoginPane()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
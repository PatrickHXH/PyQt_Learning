from PyQt5.Qt import *
import sys

class AccountTool:
    ACCOUNT_ERROR =1
    PWD_ERROR =2
    SUCCESS = 3
    def check_login(account,pwd):
        if account !="sz":
            return AccountTool.ACCOUNT_ERROR
        if pwd !=  "itlike":
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS

class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
        self.set_ui()
        self.setMinimumSize(400,400)

    def set_ui(self):
        # 展示内容
        self.account_le = QLineEdit(self)
        self.account_le.setPlaceholderText("请输入账号...")
        self.pwd_le = QLineEdit(self)
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.pwd_le.setPlaceholderText("请输入密码...")

        self.login_btn = QPushButton("登录",self)
        self.login_btn.clicked.connect(self.login_cao)

        #设置密码文本框显示清空按钮
        self.pwd_le.setClearButtonEnabled(True)

        action = QAction(QIcon("close.png"), "测试", self.pwd_le)
        def change():
            if self.pwd_le.echoMode() == QLineEdit.Normal:
                self.pwd_le.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon("close.png"))
            else:
                #明文显示
                self.pwd_le.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon("open.png"))

        #添加自定义行为，控制密码文本框密文和明文显示
        self.pwd_le.addAction(action,QLineEdit.LeadingPosition)
        action.triggered.connect(change)

        #文本提示框输入后显示候选字符串
        completer = QCompleter(["sz","shunzi","wangzha"])
        self.account_le.setCompleter(completer)

    def login_cao(self):
        print("xxx",self)
        #获取账号密码信息
        account = self.account_le.text()
        pwd = self.pwd_le.text()

        state = AccountTool.check_login(account,pwd)
        if state == AccountTool.ACCOUNT_ERROR:
            print("账号错误")
            self.account_le.setText("")
            self.pwd_le.setText("")
            self.account_le.setFocus()
            return None
        if state == AccountTool.PWD_ERROR:
            print("密码错误")
            self.pwd_le.setText("")
            self.pwd_le.setFocus()
            return None
        print("登录成功")
        # if account=="sz":
        #     if pwd=="itlike":
        #         print("登录成功")
        #     else:
        #         print("密码错误")
        #         self.pwd_le.setText("")
        #         self.pwd_le.setFocus()
        # else:
        #     print("账号错误")
        #     self.account_le.setText("")
        #     self.pwd_le.setText("")
        #     self.account_le.setFocus()

    def resizeEvent(self, evt):
        widget_w = 200
        widget_h = 40
        margin =60
        self.account_le.resize(widget_w,widget_h)
        self.pwd_le.resize(widget_w,widget_h)
        self.login_btn.resize(widget_w,widget_h)

        x = (self.width()-widget_w) // 2
        self.account_le.move(x,self.height() // 4)
        self.pwd_le.move(x,self.account_le.y()+ widget_h + margin)
        self.login_btn.move(x,self.pwd_le.y() + widget_h + margin)

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    # window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
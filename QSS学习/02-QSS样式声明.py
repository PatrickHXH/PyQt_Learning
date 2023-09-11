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
        label = QCheckBox("复选框",self)
        label.resize(1000,1000)
        label.move(50,50)

        self.qss边框(label)

                #border-width:26px;
                #border-style:solid;
                #border-radius: 90px;
                #border-image:url(../basestudy/open.png) 10px 10px 10px 10px round;
    def qss边框(self,label):
            label.setStyleSheet("""
                QCheck 
            """)

            return  None
            label.setStyleSheet("""
                QSpinBox {
                    font-size:26px;
                    color:orange;
                    border:10px double red;
                    border-radius:10px;
                    background-color:lightgrey
                }
                QSpinBox::up-button,QSpinBox::down-button{
                    width:50px;
                    height:50px;
                    
                }
                QSpinBox::up-button{
                    subcontrol-origin:padding;
                    subcontrol-position:left center
                }
                QSpinBox::up-button:hover{
                    bottom:10px
                }
                QSpinBox::down-button{
                    subcontrol-origin:padding;
                    subcontrol-position:right center
                }
            """)
            # label.setStyleSheet("""
            #     QTextEdit {
            #         font-family:隶书;
            #         color:orange
            #     }
            # """)
            # label.setStyleSheet('''
            # QTextEdit {
            #     background-color: qlineargradient(x1:0 , y1:0 ,x2:1, y2:1,stop:0 red,stop:0.4 gray,stop:1 green);
            #     background-image:url(../basestudy/test.png);
            #     background-repeat:no repeat;
            #     background-position:right bottom;
            #     background-origin:border;
            #     background-clip:padding;
            #     background-attachment:fixed;
            #
            #     color:red;
            #     border:20px double red;
            #     padding:20px;
            #     margin:20px;
            #     padding-top:150px
            # }
            # ''')



if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
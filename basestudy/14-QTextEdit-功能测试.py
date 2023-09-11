from PyQt5.Qt import *
import sys

class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())
        link_str = self.anchorAt(me.pos())
        if len(link_str) > 0:
            QDesktopServices.openUrl(QUrl(link_str))
        return super().mousePressEvent(me)

class Window(QWidget):
    def __init__(self):
        #继承Qwidget
        super().__init__()
        # 设置窗口参数
        self.setWindowTitle("黄侠侠第一个桌面窗口")
        self.resize(1500,1500)
    def text_change(self):
        print("文本内容发生了改变")
    def selection_change(self):
        print("文本选中的内容发生了改变")
    def copy_a(self, yes):
        print("复制是否可用", yes)
    def set_ui(self):
        # 展示内容
        te = MyTextEdit(self)
        self.te = te
        te.move(50,50)
        te.resize(300,300)
        te.setStyleSheet("background-color:cyan")
        # self.文本内容的设置()
        te.textChanged.connect(self.text_change)
        # te.selectionChanged.connect(self.selection_change)
        te.copyAvailable.connect(self.copy_a)
        btn = QPushButton("按钮",self)
        btn.move(10,10)
        btn.clicked.connect(self.test_button)
        #参数设置
        # tlf = QTextListFormat()
        # #缩进3个tab
        # tlf.setIndent(3)
        # tlf.setNumberPrefix("<<")
        # tlf.setNumberSuffix(">>")
        # tlf.setStyle(QTextListFormat.ListDecimal)
        # # tc.insertList(tlf)
        # self.te.textCursor().createList(tlf)

        # te.insertHtml("xxx " * 300 + "<a name='lk' href='#itlike'>撩课</a>" + "aaa" * 200)
        te.insertHtml("xxx " * 300 + "<a href='http://www.itlike.com'>撩课</a>" + "aaa" * 200)
    def test_button(self):
        # self.te.setText("")
        # print(self.te.document())
        # print(self.te.textCursor())
        # self.格式设置和合并()
        # self.内容和格式的获取()
        # self.文本选中和清空()
        # self.文本的其他操作()
        # self.文本字符的删除()
        # self.位置相关()
        # self.开始和结束操作()
        # self.自动格式化()
        # self.软换行模式()
        # self.覆盖模式()
        # self.光标设置()
        # self.字体设置()
        # self.颜色设置()
        # self.字符设置()
        # self.常用编辑操作()
        self.打开超链接()
    def 打开超链接(self):
        pass
    def tab功能测试(self):
        # self.te.setTabChangesFocus(True)
        print(self.te.tabStopDistance())
        print(self.te.tabStopWidth())
        self.te.setTabStopDistance(100)
        pass
    def 只读设置(self):
        print(self.te.isReadOnly())
        self.te.setReadOnly(True)
        self.te.insertPlainText("itlike")
        print(self.te.isReadOnly())
        pass
    def 滚动到锚点(self):
        self.te.scrollToAnchor("lk")
        pass
    def 常用编辑操作(self):
        # self.te.copy()
        # self.te.paste()
        # self.te.selectAll()
        # self.te.setFocus()
        # QTextDocument.FindBackward
        print(self.te.find("xx", QTextDocument.FindBackward | QTextDocument.FindCaseSensitively | QTextDocument.FindWholeWords))
        self.te.setFocus()
    def 字符设置(self):
        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        tcf.setFontPointSize(20)
        tcf.setFontCapitalization(QFont.Capitalize)
        tcf.setForeground(QColor(100, 200, 150))
        self.te.setCurrentCharFormat(tcf)


        tcf2 = QTextCharFormat()
        tcf2.setFontOverline(True)
        # self.te.setCurrentCharFormat(tcf2)
        self.te.mergeCurrentCharFormat(tcf2)

        pass
    def 颜色设置(self):
        self.te.setTextBackgroundColor(QColor(200, 10, 10))
        self.te.setTextColor(QColor(10, 200, 10))
        pass

    def 字体设置(self):
        # QFontDialog.getFont()
        # self.te.setFontFamily("幼圆")
        # self.te.setFontWeight(QFont.Black)
        # self.te.setFontItalic(True)
        # self.te.setFontPointSize(30)
        # self.te.setFontUnderline(True)
        font = QFont()
        font.setStrikeOut(True)
        self.te.setCurrentFont(font)
    def 对齐方式(self):
        self.te.setAlignment(Qt.AlignCenter)
    def 光标设置(self):
        print(self.te.cursorRect(self.te.textCursor()))
        if self.te.overwriteMode():
            self.te.setOverwriteMode(False)
            self.te.setCursorWidth(1)
        else:
            self.te.setOverwriteMode(True)
            self.te.setCursorWidth(10)
    def 软换行模式(self):
        #没有软换行，保证单词完整性
       # self.te.setLineWrapMode(QTextEdit.NoWrap)
        #设置软换行，给定固定宽度
        # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.te.setLineWrapColumnOrWidth(8)
        #设置宽度同时，保证单词完整性
        self.te.setWordWrapMode(QTextOption.WordWrap)
        pass
    def 自动格式化(self):
        #变成项目列表
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)
    def 开始和结束操作(self):
        #一次性撤销操作
        tc = self.te.textCursor()
        tc.beginEditBlock()
        tc.insertText("123")
        tc.insertBlock()
        tc.insertText("456")
        tc.insertBlock()
        tc.insertText("789")
        tc.endEditBlock()

    def 位置相关(self):
        tc = self.te.textCursor()
        print("是否在段落的结尾:", tc.atBlockEnd())
        print("是否在段落的开始:", tc.atBlockStart())
        print("是否在文档的结尾:", tc.atEnd())
        print("是否在文档的开始:", tc.atStart())

        print("在第几列", tc.columnNumber())
        print("光标位置", tc.position())
        print("在文本块中的位置", tc.positionInBlock())

    def 文本字符的删除(self):
        tc = self.te.textCursor()
        tc.deleteChar()
        tc.deletePreviousChar()

    def 文本的其他操作(self):
        tc = self.te.textCursor()
        #选中的起始位置
        print(tc.selectionStart())
        print(tc.selectionEnd())

        #清除选中
        tc.clearSelection()
        self.te.setTextCursor(tc)
        self.te.setFocus()

        #删除选中文本
        tc.removeSelectedText()
        self.te.setFocus()

    def 文本选中内容的获取(self):
        tc = self.te.textCursor()
        # print(tc.selectedText())
        QTextDocumentFragment
        # print(tc.selection().toPlainText())
        print(tc.selectedTableCells())
        pass

    def 文本选中和清空(self):
        tc = self.te.textCursor()
        # tc.setPosition(6, QTextCursor.KeepAnchor)
        # tc.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor, 1)
        tc.select(QTextCursor.WordUnderCursor)
        self.te.setTextCursor(tc)

        self.te.setFocus()
        pass

    def 内容和格式的获取(self):
        tc = self.te.textCursor()
        QTextList
        # print(tc.block().text())
        # print(tc.blockNumber())
        print(tc.currentList().count())
        pass

    def 格式设置和合并(self):
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setCharFormat(tcf)

        tcf2 = QTextCharFormat()
        tcf2.setFontStrikeOut(True)
        # tc.setCharFormat(tcf2)
        tc.mergeCharFormat(tcf2)

        return None
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)
        tbf.setIndent(2)
        tc.setBlockFormat(tbf)

        return None
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setBlockCharFormat(tcf)
    def 光标插入内容(self):
        #插入文本框架
        tc = self.te.textCursor()
        tff = QTextFrameFormat()
        tff.setBorder(10)
        tff.setBorderBrush(QColor(100,50,50))
        print(tc.insertFrame(tff))

        #加入子框架
        doc =self.te.document()
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat(tff)

        return None
        #插入文本块
        tc = self.te.textCursor()
        #设置文本块参数
        tbf = QTextBlockFormat()
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶属")
        tcf.setFontPointSize(60)
        tbf.setAlignment(Qt.AlignRight)
        tbf.setRightMargin(100)
        tc.insertBlock(tbf,tcf)
        self.te.setFocus()

        return None
        #插入表格
        tc = self.te.textCursor()
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        ttf.setCellPadding(6)
        ttf.setCellSpacing(3)
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength,50),
                                       QTextLength(QTextLength.PercentageLength, 30),
                                       QTextLength(QTextLength.PercentageLength, 20),
                                       ))
        table = tc.insertTable(5,3,ttf)
        #追加列
        # table.appendColumns(2)

        return None
        #插入列表，创建列表
        tc = self.te.textCursor()
        #参数设置
        tlf = QTextListFormat()
        #缩进3个tab
        tlf.setIndent(3)
        tlf.setNumberPrefix("<<")
        tlf.setNumberSuffix(">>")
        tlf.setStyle(QTextListFormat.ListDecimal)
        # tc.insertList(tlf)
        tc.createList(tlf)

        return  None
        #插入句子
        tc = self.te.textCursor()
        tdf = QTextDocumentFragment.fromHtml("<h1>123</h1>")
        tc.insertFragment(tdf)

        return None
        #插入图片参数
        tc =  self.te.textCursor()
        tif =QTextImageFormat()
        tif.setName("test.png")
        tif.setHeight(100)
        tif.setWidth(100)
        tc.insertImage(tif)

        #靠右浮动
        tc.insertImage(tif,QTextFrameFormat.FloatRight)
        #插入图片，可不用
        # tc.insertImage("test.png")

        return None
        #插入字体
        tcf = QTextCharFormat()
        tcf.setToolTip("测试提示")
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(25)

        tc = self.te.textCursor()
        tc.insertText("itlike.com",tcf)

    def 文本内容的设置(self):
        #设置普通文本的内容
        # self.te.setPlainText("<h1>xxxx</h1>")
        # self.te.insertPlainText("<h1>你好</h1>")
        # print(self.te.toPlainText())

        self.te.setHtml("<h1>你好</h1>")
        self.te.append("末尾追加")

    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入个人简介")
        print(self.te.placeholderText())

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建应用程序对象
    # 默认应用程序对象可使用qApp,相当于全局变量
    window = Window()
    window.set_ui()
    window.show()
    sys.exit(app.exec())  #app.exec()进入无限消息循环，监听用户动作
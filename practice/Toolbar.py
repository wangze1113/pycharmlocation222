'''
创建的使用工具栏

工具栏默认按钮：只显示图标，将文本作为悬停提示提示
工具栏按钮有三种显示状态：
1.只显示图标
2.只显示文本
3.同时显示文本和图标


'''

import sys,math
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Toolbar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300,200)

        tb1=self.addToolBar("File")

        new=QAction(QIcon('file.jpg'),"new",self)
        tb1.addAction(new)

        open=QAction(QIcon('open.jpg'),"open",self)
        tb1.addAction(open)

        save=QAction(QIcon('save.jpg'),"save",self)
        tb1.addAction(save)

        tb2=self.addToolBar("File2")
        new2=QAction(QIcon('file.jpg'),"新建",self)
        tb2.addAction(new2)

        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)#设置文字在图片的方位

        tb1.actionTriggered.connect(self.toolbtnpressed)
        tb2.actionTriggered.connect(self.toolbtnpressed)
    def toolbtnpressed(self,a):
        print("按下的工具栏按钮是",a.text())

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=Toolbar()
    main.show()

    sys.exit(app.exec_())
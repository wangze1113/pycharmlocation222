import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QWidget,QPushButton
from PyQt5.QtCore import pyqtSlot
class QuitApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        #添加button
        self.button1=QPushButton('退出应用程序')
        #关联信号与槽
        self.button1.clicked.connect(lambda:self.onClick_Button())
        #水平布局
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    #按钮单击事件的方法

    def onClick_Button(self):
        sender=self.sender()
        print('按钮被按下')
        app=QApplication.instance()
        #退出程序
        app.quit()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QuitApplication()
    main.show()

    sys.exit(app.exec_())
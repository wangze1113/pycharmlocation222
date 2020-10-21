import sys
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QWidget,QPushButton,QToolTip,QMainWindow
from PyQt5.QtGui import QFont

class ToolTip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('simSun',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300,300,250,250)
        self.setWindowTitle('设置控件提示消息')

        self.button1=QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮,are you ok?')
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ToolTip()
    main.show()

    sys.exit(app.exec_())
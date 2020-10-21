import sys
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication
from PyQt5.QtGui import QIcon

class IconFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,250)
        self.setWindowTitle('设置窗口图标')
        #self.setWindowIcon(QIcon('practice/320085404332.png'))

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('320085404332.png'))
    main=IconFrame()
    main.show()

    sys.exit(app.exec_())
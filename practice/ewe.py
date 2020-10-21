import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("第一个主窗口应用")
        self.resize(400,400)

        self.status=self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('320085404332.png'))
    main=FirstMainWin()
    main.show()

    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import *

class QLineEditeEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formlayout=QFormLayout()

        normalLineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit=QLineEdit()
        passwordEchoLineEdit=QLineEdit()

        formlayout.addRow("Normal",normalLineEdit)
        formlayout.addRow("NoEcho",noEchoLineEdit)
        formlayout.addRow("Password",passwordLineEdit)
        formlayout.addRow("PasswordEchoLineEdit",passwordEchoLineEdit)

        #placeholdtext(灰色字体)
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("noEchoLineEdit")
        passwordLineEdit.setPlaceholderText("passwordLineEdit")
        passwordEchoLineEdit.setPlaceholderText("passwordEchoEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditeEchoMode()
    main.show()

    sys.exit(app.exec_())
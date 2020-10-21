import sys
from PyQt5.QtWidgets import *

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')
        nameLalbel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
        #设置伙伴控件
        nameLalbel.setBuddy(nameLineEdit)

        passwordLalbel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLalbel.setBuddy(passwordLineEdit)

        btnOK=QPushButton('&OK')
        btnCancle=QPushButton('&Cancle')

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLalbel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLalbel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancle,2,2)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLabelBuddy()
    main.show()

    sys.exit(app.exec_())
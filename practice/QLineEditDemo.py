import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit1=QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setFont(QFont('Arial',10))

        edit2=QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3=QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4=QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5=QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6=QLineEdit('hello，酷酷酷')
        edit6.setReadOnly(True)



        formlayout=QFormLayout()
        formlayout.addRow('整数校验',edit1)
        formlayout.addRow('浮点型',edit2)
        formlayout.addRow('Input Mask',edit3)
        formlayout.addRow('文本变化',edit4)
        formlayout.addRow('密码',edit5)
        formlayout.addRow('只读',edit6)
        self.setLayout(formlayout)
        self.setWindowTitle('QLineEdit综合案例')

    def textChanged(self,text):
        print('输入的内容：'+text)

    def enterPress(self):
        print('已输入内容')


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditDemo()
    main.show()

    sys.exit(app.exec_())
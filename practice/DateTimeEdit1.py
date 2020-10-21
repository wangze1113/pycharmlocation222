'''

输入各种风格的日期和时间

QDateTimeEdit
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DateTimeEdit1(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vlayout=QVBoxLayout()
        dateTimeEdit1=QDateTimeEdit()
        dateTimeEdit2=QDateTimeEdit(QDateTime.currentDateTime())

        dateEdit=QDateTimeEdit(QDate.currentDate())
        timeEdit=QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        self.setLayout(vlayout)

        self.resize(300,90)
        self.setWindowTitle("设置不同风格的日期和时间")

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DateTimeEdit1()
    main.show()
    sys.exit(app.exec_())
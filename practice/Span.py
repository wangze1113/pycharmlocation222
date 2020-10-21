'''

合并单元格

setSpan(row,col,要合并的行数，要合并的列数)

'''

import sys
from PyQt5.QtWidgets import *

class Span(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("合并单元格")
        self.resize(500,500)
        layout=QHBoxLayout()
        tableWidge=QTableWidget()
        tableWidge.setRowCount(4)
        tableWidge.setColumnCount(3)
        layout.addWidget(tableWidge)

        tableWidge.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])

        newItem=QTableWidgetItem('雷神')
        tableWidge.setItem(0,0,newItem)
        tableWidge.setSpan(0,0,3,1)

        newItem = QTableWidgetItem('男')
        tableWidge.setItem(0, 1, newItem)
        tableWidge.setSpan(0, 1, 2, 1)

        newItem = QTableWidgetItem('123')
        tableWidge.setItem(0, 2, newItem)
        tableWidge.setSpan(0, 2, 4, 1)

        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=Span()
    main.show()
    sys.exit(app.exec_())
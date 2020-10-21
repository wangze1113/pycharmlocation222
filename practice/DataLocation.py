'''

在表格中快速定位到特定的行

1.数据的定位：findItem
2.如果找到了满足条件的单元格，会定位到单元格所在的行：setSliderposition

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

class DataLocation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidge 例子")
        self.resize(600,800)

        layout=QHBoxLayout()
        tableWidge=QTableWidget()
        tableWidge.setRowCount(40)
        tableWidge.setColumnCount(4)

        layout.addWidget(tableWidge)

        for i in range(40):
            for j in range(4):
                itemContent='(%d,%d)'%(i,j)
                tableWidge.setItem(i,j,QTableWidgetItem(itemContent))
            self.setLayout(layout)

            #搜素满足条件的Cell
            text='(13,1)'
            items=tableWidge.findItems(text,QtCore.Qt.MatchExactly)
            if len(items)>0:
                item=items[0]
                item.setBackground(QBrush(QColor(0,255,0)))
                item.setBackground(QBrush(QColor(255,0,0)))

                row=item.row()
                #定位到指定的行
                tableWidge.verticalScrollBar().setSliderPosition(row)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DataLocation()
    main.show()
    sys.exit(app.exec_())
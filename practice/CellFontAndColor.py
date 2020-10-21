'''

设置单元格字体和颜色

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CellFontAndColor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(430,230)
        layout=QHBoxLayout()
        tableWidge=QTableWidget()
        tableWidge.setRowCount(4)
        tableWidge.setColumnCount(3)
        layout.addWidget(tableWidge)

        tableWidge.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])

        newItem=QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',14,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidge.setItem(0,0,newItem)

        newItem = QTableWidgetItem('死亡女神')
        newItem.setBackground(QBrush(QColor(255,255,0)))
        newItem.setForeground(QBrush(QColor( 0, 0,255)))
        tableWidge.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('16')
        newItem.setFont(QFont('Times', 21, QFont.Black))
        newItem.setForeground(QBrush(QColor( 0, 0,255)))
        tableWidge.setItem(0, 2, newItem)

        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=CellFontAndColor()
    main.show()
    sys.exit(app.exec_())
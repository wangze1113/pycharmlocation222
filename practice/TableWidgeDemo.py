'''

扩展的表格控件（QTableWidge）

QTableView

每一个cell（单元格）是一个QTableWidgeItem
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TableWidgeDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidge演示")
        self.resize(430,230)
        layout=QHBoxLayout()
        tablewidge=QTableWidget()
        tablewidge.setRowCount(4)
        tablewidge.setColumnCount(3)

        layout.addWidget(tablewidge)

        tablewidge.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem=QTableWidgetItem("小明")
        nameItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        tablewidge.setItem(0,0,nameItem)

        ageItem = QTableWidgetItem("20")
        ageItem.setTextAlignment(Qt.AlignLeft | Qt.AlignBottom)
        tablewidge.setItem(0, 1, ageItem)

        jgItem = QTableWidgetItem("小明")
        tablewidge.setItem(0, 2, jgItem)

        #禁止编辑
        tablewidge.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #整行选择
        tablewidge.setSelectionBehavior(QAbstractItemView.SelectRows)

        #调整行和列
        #tablewidge.resizeColumnsToContents()
        #tablewidge.resizeRowsToContents()

        #隐藏行头
        #tablewidge.horizontalHeader().setVisible(False)
        #隐藏列头
        #tablewidge.verticalHeader().setVisible(False)

        tablewidge.setVerticalHeaderLabels(["a","b"])

        #隐藏表格线
        #tablewidge.setShowGrid(False)

        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=TableWidgeDemo()
    main.show()
    sys.exit(app.exec_())

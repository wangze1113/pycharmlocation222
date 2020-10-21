'''

按列排序

1.按哪一列排序
2.排序类型：升序或降序

sortItems(columIndex,orderType)

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ColumSort(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("案列排序")
        self.resize(430,230)
        layout=QVBoxLayout()
        self.tablewidge=QTableWidget()
        self.tablewidge.setRowCount(4)
        self.tablewidge.setColumnCount(3)
        layout.addWidget(self.tablewidge)

        self.tablewidge.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])

        newItem=QTableWidgetItem('张三')
        self.tablewidge.setItem(0,0,newItem)

        newItem = QTableWidgetItem('男')
        self.tablewidge.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('100')
        self.tablewidge.setItem(0, 2, newItem)

        newItem = QTableWidgetItem('李四')
        self.tablewidge.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tablewidge.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('60')
        self.tablewidge.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王二')
        self.tablewidge.setItem(2, 0, newItem)

        newItem = QTableWidgetItem('女')
        self.tablewidge.setItem(2, 1, newItem)

        newItem = QTableWidgetItem('80')
        self.tablewidge.setItem(2, 2, newItem)

        self.button=QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType=Qt.DescendingOrder
        self.setLayout(layout)

    def order(self):
        if self.orderType==Qt.DescendingOrder:
            self.orderType=Qt.AscendingOrder
        else:
            self.orderType=Qt.DescendingOrder

        self.tablewidge.sortItems(2,self.orderType)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ColumSort()
    main.show()
    sys.exit(app.exec_())
'''
显示二维表数据（QTableView控件）
数据源
model

需要创建QTableView实例和一个数据源（modle）,然后将两者关联

MVC
MVC的目的是将后端的数据和前端页面的耦合度降低
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTableView表格视图控件演示')
        self.resize(500,300)

        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['id','姓名','年龄'])

        self.tableview=QTableView()
        #关联QTableView控件和Model
        self.tableview.setModel(self.model)

        #添加数据
        item11=QStandardItem('10')
        item12=QStandardItem('雷神')
        item13=QStandardItem('2000')
        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)



        layout=QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=TableView()
    main.show()

    sys.exit(app.exec_())
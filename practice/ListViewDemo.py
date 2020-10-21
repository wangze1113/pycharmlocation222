'''
显示列表数据（QListView控件）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class ListViewDemo(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('QListView例子')
        self.resize(300,270)
        layout=QVBoxLayout()

        listview=QListView()
        listModel=QStringListModel()
        self.list=["列表项1","列表项2","列表项3"]

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,"QListView","您选择了： "+self.list[item.row()])

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ListViewDemo()
    main.show()
    sys.exit(app.exec_())
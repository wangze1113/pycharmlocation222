'''

树控件（QTreeWidge）的基本用法
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BasicTreeWidge(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("树控件（QTreeWidge）的基本用法")

        self.tree=QTreeWidget()
        self.tree.setColumnCount(2)
        #指定列标签
        self.tree.setHeaderLabels(['Key','Value'])

        root=QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('320085404332.png'))
        self.tree.setColumnWidth(0,160)

        #添加子节点
        child1=QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点1的数据')
        child1.setCheckState(0,Qt.Checked)

        #添加子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setText(1,'子节点2的数据')

        #为子节点2添加一个子节点
        child3=QTreeWidgetItem(child2)
        child3.setText(0,'子节点2的子节点')
        child3.setText(1,'子节点2的子节点的数据')

        #设置节点全部展开
        self.tree.expandAll()
        
        self.setCentralWidget(self.tree)


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=BasicTreeWidge()
    main.show()
    sys.exit(app.exec_())
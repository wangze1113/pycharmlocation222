'''

添加，修改和删除树控件的节点

'''

import sys
from PyQt5.QtWidgets import *

class ModifyTree(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TreeWidge 例子")

        operatorLayout=QHBoxLayout()
        addButton=QPushButton('添加节点')
        updateButton=QPushButton('修改节点')
        deleteButton=QPushButton('删除节点')

        operatorLayout.addWidget(addButton)
        operatorLayout.addWidget(updateButton)
        operatorLayout.addWidget(deleteButton)

        addButton.clicked.connect(self.addNode)
        updateButton.clicked.connect(self.updateNode)
        deleteButton.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()

        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)

        root.setText(0, 'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '1')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '1')
        self.tree.clicked.connect(self.onTree)

        mainLayout=QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)
 

    def onTree(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0), item.text(1)))

    def addNode(self):
        print('添加节点')
        item=self.tree.currentItem()
        print(item)
        node=QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新值')

    def updateNode(self):
        print('修改节点')
        item=self.tree.currentItem()
        item.setText(0,'修改节点')
        item.setText(1,'值已经被修改')


    def deleteNode(self):
        print('删除节点')
        item=self.tree.currentItem()
        root=self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ModifyTree()
    main.show()
    sys.exit(app.exec_())

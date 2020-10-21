'''

扩展的列表控件（QListWidge）

'''
from PyQt5.QtWidgets import *
import sys

class ListWidgeDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidge 例子")
        self.resize(300,200)

        self.listwidge=QListWidget()
        self.listwidge.addItem("item1")
        self.listwidge.addItem("item2")
        self.listwidge.addItem("item3")
        self.listwidge.addItem("item4")
        self.listwidge.addItem("item5")
        self.listwidge.itemClicked.connect(self.clicked)
        self.setCentralWidget(self.listwidge)

    def clicked(self,Index):
        QMessageBox.information(self,"QListWidge","您选择了："+self.listwidge.item(self.listwidge.row(Index)).text())

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ListWidgeDemo()
    main.show()
    sys.exit(app.exec_())
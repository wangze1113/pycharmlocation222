'''
让控件支持拖拽动作

A.setAcceptDrops(True)
A拖到B
B.setAcceptDraps(True)

B需要两个事件
1，dragEnterEvent  将A拖到B触发
2。dropEvent  在b的区域放下A时触发
'''
import sys,math
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyComBox(QComboBox):   #扩展控件
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super().__init__()
        formlayout=QFormLayout()
        formlayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)#让QlineEdit控件可拖动

        combo=MyComBox()
        formlayout.addRow(lineEdit,combo)
        self.setLayout(formlayout)
        self.setWindowTitle('拖拽案例')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrapDropDemo()
    main.show()
    sys.exit(app.exec_())
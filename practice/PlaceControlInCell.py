'''

在单元格中放置控件

setItem:将文本放到单元格中
setCellWidge:将控件放到单元格中
setStyleSheet:设置控件的样式（QSS）

setCellWidge

'''
import sys
from PyQt5.QtWidgets import *

class PlaceContolInCell(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430,300)
        layout=QHBoxLayout()
        tableWidge=QTableWidget()
        tableWidge.setRowCount(4)
        tableWidge.setColumnCount(3)

        layout.addWidget(tableWidge)

        tableWidge.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        textItem=QTableWidgetItem('小明')
        tableWidge.setItem(0,0,textItem)

        combox=QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        #QSS类似于CSS  Qt StyleSheet
        combox.setStyleSheet('QComboBox{margin:3px};')
        tableWidge.setCellWidget(0,1,combox)

        modifyButton=QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidge.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=PlaceContolInCell()
    main.show()
    sys.exit(app.exec_())
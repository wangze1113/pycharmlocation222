import sys
from PyQt5.QtWidgets import *

class QLineEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formlayout=QFormLayout()

        ipLineEdit=QLineEdit()
        macEdit=QLineEdit()
        dateEdit=QLineEdit()
        licenseLineEdit=QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000;_')
        macEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')  #没有输入时用_代替
        dateEdit.setInputMask('0000-00-00;_')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA;#')  #没有输入时用#代替

        formlayout.addRow('数字掩码',ipLineEdit)
        formlayout.addRow('mac掩码',macEdit)
        formlayout.addRow('日期掩码',dateEdit)
        formlayout.addRow('许可证掩码',licenseLineEdit)

        self.setLayout(formlayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditMask()
    main.show()

    sys.exit(app.exec_())
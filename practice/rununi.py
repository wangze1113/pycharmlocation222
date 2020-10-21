import sys
import untitled
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainwindow=QMainWindow()
    ui=untitled.Ui_Dialog()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
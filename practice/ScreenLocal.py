import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QHBoxLayout,QApplication,QPushButton
def onClick_Button():
    print("onclick")
app=QApplication(sys.argv)

widget=QWidget()
btn=QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(lambda:onClick_Button())

btn.move(24,25)
widget.resize(300,240) #工作区的尺寸
widget.move(250,200)  #

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())


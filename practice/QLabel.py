import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QVBoxLayout,QLabel
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签,</font>")
        label1.setAutoFillBackground(True)
        patette=QPalette()
        patette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)  #对齐方式

        label2.setText("<a href='#'>欢迎使用Python </a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("320085404332.png"))
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox=QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2')
    def linkClicked(self):
        print('当鼠标单击label4标签时')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLable()
    main.show()

    sys.exit(app.exec_())

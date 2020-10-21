#必须在paintEvent事件中绘制各种元素

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont

class DrawText(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(400,300)
        self.text='菜鸟'

    def paintEvent(self,event):
        painter=QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(150,42,5))
        painter.setFont(QFont('SimSun',25))

        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawText()
    main.show()

    sys.exit(app.exec_())
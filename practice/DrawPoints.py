import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DrawPoints(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('在窗口上用像素点绘制两个周期的正弦曲线')
        self.resize(300,300)

    def paintEvent(self, event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.red)
        size=self.size()

        for i in range(1000):
            x=100*(-1+2.0*i/1000)+size.width()/2.0
            y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
            painter.drawPoint(x,y)

        painter.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawPoints()
    main.show()

    sys.exit(app.exec_())
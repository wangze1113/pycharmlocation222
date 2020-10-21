import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DrawAll(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘制各种图形')
        self.resize(600,900)

    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)

        #绘制弦
        rect=QRect(0,10,100,100)
        #alen:1个alen等于1/16度，   45*16
        qp.drawArc(rect,0,50*16)

        #通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120,10,100,100,0,360*16)
        #绘制带弦的弧
        qp.drawChord(10,120,100,100,12,130*16)
        #绘制扇形
        qp.drawPie(10,240,100,100,12,130*16)
        #绘制椭圆
        qp.drawEllipse(120,120,150,100)  #可以绘制圆
        #绘制五边形
        point1=QPoint(340,380)
        point2 = QPoint(470, 420)
        point3= QPoint(490, 512)
        point4 = QPoint(490, 588)
        point5 = QPoint(400, 533)

        polygon=QPolygon([point1,point2,point3,point4,point5])
        qp.drawPolygon(polygon)

        #绘制图像
        image=QImage('320085404332.png')
        rect=QRect(10,400,image.width()/3,image.height()/3)
        qp.drawImage(rect,image)
        qp.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawAll()
    main.show()
    sys.exit(app.exec_())
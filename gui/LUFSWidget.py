from PyQt5 import Qt


class LUFSWidget(Qt.QWidget):

    sliderPos=-25
    def __init__(self):
        super().__init__()

    def paintEvent(self, *args, **kwargs):
        x1 = 5
        y1 = 15
        x2 = 50
        y2=230+y1
        qp = Qt.QPainter()
        qp.begin(self)
        qp.setBrush(Qt.QColor(245,202,200))

        qp.setPen(Qt.QColor(120,21,26))
 
        qp.drawRect(x1, y1, x2, y2)

        qp.drawLine(x1,y1+((5/59)*y2),x2+5,y1+((5/59)*y2))
        qp.drawLine(x1,y1+((14/59)*y2),x2+5,y1+((14/59)*y2))
        qp.drawLine(x1,y1+((23/59)*y2),x2+5,y1+((23/59)*y2))
        qp.drawLine(x1,y1+((41/59)*y2),x2+5,y1+((41/59)*y2))

        #labels
        qp.setPen(Qt.QColor(255,255,255))
        qp.drawText(x2+7, y1-2,"0")
        qp.drawText(x2+7, y1+((5/59)*y2),"-5")
        qp.drawText(x2+7, y1+((14/59)*y2),"-14")
        qp.drawText(x2+7, y1+((23/59)*y2),"-23")   
        qp.drawText(x2+7, y1+((41/59)*y2),"-41")  
        qp.drawText(x2+7, y1+y2,"-59")  

        #slider
        if (self.sliderPos<=-22) and (self.sliderPos>=-24):
            qp.setBrush(Qt.QColor(65, 205, 82,128))
            qp.setPen(Qt.QColor(65, 205, 82,128))
        else:
            qp.setBrush(Qt.QColor(120,21,26,128))
            qp.setPen(Qt.QColor(120,21,26,128))

        realSliderPos = y1+((abs(self.sliderPos/59))*y2)
        qp.drawRect(x1-5, realSliderPos-2, x2+10, 4)
        qp.end()
        return Qt.QWidget.paintEvent(self, *args, **kwargs)

    def setPos(self,pos):
        self.sliderPos=pos
        self.update()

#if __name__ == '__main__':
#    app = Qt.QApplication([])
#    w = Widget()
#    w.show()
#    app.exec()

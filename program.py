import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randrange

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_circle()
            self.qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self):
        self.qp.setBrush(QColor(255, 255, 0))
        r = randrange(10, 100, 1)
        x = randrange(r, 401 - r, 1)
        y = randrange(r, 331 - r, 1)
        self.qp.drawEllipse(x, y, r, r)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
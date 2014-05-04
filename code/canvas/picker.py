import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QGraphicsScene, QGraphicsView, QGraphicsPolygonItem

class Picker(QGraphicsView):
    def __init__(self, scene):
        super(Picker, self).__init__(scene)
        self.setDragMode(QGraphicsView.RubberBandDrag)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    scn = QGraphicsScene()
    scn.addEllipse(0, 0, 250, 100)
    p = Picker(scn)
    p.show()

    sys.exit(app.exec_())

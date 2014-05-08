import json
from maya import cmds
from PySide import QtGui, QtCore
from qt_utils import get_anchor


class Polygon(QtGui.QGraphicsPolygonItem):
    NO_BRUSH = QtGui.QBrush()

    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)
        self.name = ""
        self.targets = list()

    @property
    def color(self):
        c = self.brush().color()
        return (c.red(), c.green(), c.blue())

    @color.setter
    def color(self, color):
        b = QtGui.QBrush(QtGui.QColor(*color)) if color else self.NO_BRUSH
        self.setBrush(b)  # polygon color
        p = self.pen()
        p.setBrush(self.NO_BRUSH)  # no border line
        self.setPen(p)

    @classmethod
    def fromPoints(cls, points):
        points = QtGui.QPolygonF([QtCore.QPointF(*p) for p in points])
        return cls(points)


class Picker(QtGui.QGraphicsView):

    def __init__(self, *args, **kwargs):
        super(Picker, self).__init__(*args, **kwargs)
        self.setInteractive(True)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)

    def loadData(self, data):
        self.scene().clear()
        for d in data["selectors"]:
            p = Polygon.fromPoints(d["points"])
            p.name = d["name"]
            p.color = [int(x * 255)
                       for x in data["color_table"].get(d["color"])]
            p.targets.extend([data["anim_table"].get(x) for x in d["targets"]])
            p.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
            self.scene().addItem(p)

    def select(self, target, mod):
        if not len(target):
            return cmds.select(cl=True)
        ctrl = int(QtCore.Qt.ControlModifier)
        shift = int(QtCore.Qt.ShiftModifier)
        flags = {"r": mod == 0,
                 "d": mod == ctrl,
                 "tgl": mod == shift,
                 "add": mod == ctrl + shift}
        cmds.select(target, **flags)

    def resizeEvent(self, event):
        self.fitInView(self.scene().sceneRect(), QtCore.Qt.KeepAspectRatio)

    def mouseReleaseEvent(self, event):
        super(Picker, self).mouseReleaseEvent(event)
        targets = [y for x in self.scene().selectedItems() for y in x.targets]
        self.select(targets, int(event.modifiers()))
        self.scene().clearSelection()


def from_json(json_file):
    with open(json_file) as fp:
        data = json.load(fp)
    return data


def open_picker(data):
    app = QtGui.QMainWindow(parent=get_anchor())
    app.setWindowTitle("Character Picker")
    p = Picker()
    p.setScene(QtGui.QGraphicsScene())
    p.loadData(data)
    app.setCentralWidget(p)
    app.show()


d = from_json(r"W:\slides\slides_picker\code\canvas\dummy2.json")
if d.get("filetype") == "picker_data" and d.get("version") >= 0.2:
    open_picker(d)

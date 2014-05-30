import os
import json

from PySide.QtGui import QMainWindow
from maya import cmds

from . import dummy
from ..qt_utils import get_anchor


class Picker(QMainWindow):

    def __init__(self, parent, data):
        super(Picker, self).__init__(parent)
        self.ui = dummy.Ui_MainWindow()
        self.ui.setupUi(self)
        # SIGNALS
        for k, v in data["anim_table"].iteritems():
            if hasattr(self.ui, k):
                getattr(self.ui, k).clicked.connect(lambda t=v: self.select(t))
        self.ui.select_all.clicked.connect(
            lambda t=data["anim_table"].values(): self.select(t))

    def select(self, target):
        shift, ctrl = 1, 4
        mod = int(cmds.getModifiers())
        flags = {"replace": mod == 0,
                 "toggle": mod == shift,
                 "deselect": mod == ctrl,
                 "add": mod == ctrl + shift}
        cmds.select(target, **flags)


def show():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "mario.json")
    with open(path) as fp:
        d = json.load(fp)
    if d.get("filetype") == "picker_data" and d.get("version") >= 0.1:
        Picker(parent=get_anchor(), data=d).show()

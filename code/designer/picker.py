import json
from PySide.QtGui import QDialog
from dummy import Ui_Dialog
from qt_utils import get_anchor
from maya import cmds


class Picker(QDialog):

    def __init__(self, parent, data):
        super(Picker, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # signals
        for k, v in data["anim_table"].iteritems():
            if hasattr(self.ui, k):
                getattr(self.ui, k).clicked.connect(
                    lambda target=v: cmds.select(target))
        self.ui.select_all.clicked.connect(
            lambda target=data["anim_table"].values(): cmds.select(target))


def from_json(json_file):
    with open(json_file) as fp:
        data = json.load(fp)
    return data


def open_picker(data):
    picker = Picker(parent=get_anchor(), data=d)
    picker.show()

d = from_json(r"W:\slides\slides_picker\code\cmds\data.json")
if d.get("filetype") == "picker_data" and d.get("version") >= 0.1:
    open_picker(d)

from .cmds import picker_v2 as cmds_picker
from .designer import picker as designer_picker
from .canvas import picker as canvas_picker


def show(picker_type="designer"):
    {"cmds": cmds_picker.show,
     "designer": designer_picker.show,
     "canvas": canvas_picker.show}.get(picker_type)()

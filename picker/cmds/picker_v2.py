import os
import json

from maya import cmds  # importamos los comandos de maya


def picker(data, w=300, h=30):
    p = cmds.window(title="Picker", width=w)  # nueva ventana
    cmds.columnLayout(adjustableColumn=True)  # layout vertical
    # nombre del personaje
    cmds.text(label="char: " + data["charname"], height=h)
    # botones
    for btn in data["selectors"]:
        # obtenemos targets
        targets = [data["anim_table"].get(x) for x in btn["targets"]]
        color = [c / 255.0 for c in data["color_table"].get(btn["color"])]
        # creamos el boton
        cmds.button(label=btn["name"], height=h, backgroundColor=color,
                    command=lambda _, t=targets: cmds.select(t))
    cmds.showWindow(p)  # abrimos la ventana


def show():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "mario.json")
    with open(path) as fp:
        d = json.load(fp)
    if d.get("filetype") == "picker_data" and d.get("version") >= 0.1:
        picker(d)

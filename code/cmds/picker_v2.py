import json  # importamos json
from maya import cmds  # importamos los comandos de maya


def from_json(json_file):
    with open(json_file) as fp:  # abrimos json_file en modo lectura
        data = json.load(fp)  # convertimos de json a python
    return data


def open_picker(data, w=300, h=30):
    validate = (data.get("filetype") == "picker_data",
                data.get("version") >= 0.1)
    if not all(validate):  # validamos data
        return
    w = cmds.window(title="Picker", width=w)  # nueva ventana
    cmds.columnLayout(adjustableColumn=True)  # layout vertical
    # nombre del personaje
    cmds.text(label="char: " + data["charname"], height=h)
    # botones
    for btn in data["selectors"]:
        # obtenemos targets
        targets = [data["anim_table"].get(x) for x in btn["targets"]]
        # creamos el boton
        cmds.button(label=btn["name"],
                    height=h,
                    backgroundColor=data["color_table"].get(btn["color"]),
                    command=lambda _, t=targets: cmds.select(t))
    cmds.showWindow(w)  # abrimos la ventana

d = from_json(r"W:\slides\slides_picker\code\cmds\data.json")
open_picker(d)

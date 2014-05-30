import re
import sys
import json
from xml.etree import ElementTree


def get_key(key, dictionary):
    i = 1
    while key + str(i) in dictionary.keys():
        i += 1
    return key + str(i)


def main(ui_file):
    data = {"filetype": "picker_data", "version": 0.2,
            "charname": "mario_rig",
            "color_table": dict(),
            "anim_table": dict(),
            "selectors": list(),
            }
    json_file = ".".join(ui_file.split(".")[:-1]) + ".json"
    xml = ElementTree.parse(ui_file)
    for btn in xml.getroot().find("widget").find("widget").findall("widget"):
        if not btn.attrib.get("class") or "Button" not in btn.attrib.get("class"):
            continue

        d = dict()
        d["name"] = btn.attrib.get("name")
        d["targets"] = (btn.attrib.get("name"), )
        for p in btn.findall("property"):
            # color
            if p.attrib.get("name") == "styleSheet":
                regex = re.compile("background-color.*rgb(\(.*\))")
                r = regex.findall(p.find("string").text)
                color = eval(r[0]) if len(r) else None
                color = [x / 255.0 for x in color]
                for k, v in data["color_table"].iteritems():
                    if color == v:
                        d["color"] = k
                if not d.get("color"):
                    key = get_key("color", data["color_table"])
                    data["color_table"][key] = color
                    d["color"] = key
            # points
            if p.attrib.get("name") == "geometry":
                x, y, w, h = [int(x.text) for x in p.find("rect")]
                d["points"] = ((x, y), (x + w, y), (x + w, y + h), (x, y + h))
        data["selectors"].append(d)

    try:
        # reusing previous data
        with open(r"W:\slides\slides_picker\code\data\mario.json") as fp:
            d = json.load(fp)
        data["anim_table"] = d["anim_table"]
    except:
        pass

    with open(json_file, "w") as fp:
        json.dump(data, fp, indent=2, separators=[",", ":"])

if __name__ == "__main__" and len(sys.argv) == 2:
    main(sys.argv[1])

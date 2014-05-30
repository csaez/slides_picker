import sys
path = "D:\\Works\\slides\\slides_picker"
if path not in sys.path:
    sys.path.append(path)


import picker

picker.show("designer")

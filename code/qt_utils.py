from PySide.QtGui import QMainWindow  # qt widget
from shiboken import wrapInstance    # generador, parte de PySide
from maya.OpenMayaUI import MQtUtil  # utilidades Qt maya


def get_anchor():
    ptr = MQtUtil.mainWindow()  # puntero a la ventana de maya (c++)
    # retorna instancia QMainWindow desde ptr
    return wrapInstance(long(ptr), QMainWindow)

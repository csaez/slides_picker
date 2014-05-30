from maya.OpenMayaUI import MQtUtil
from shiboken import wrapInstance
from PySide.QtGui import QMainWindow


def get_anchor():
    ptr = MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QMainWindow)

import sys
import time
from PySide6 import QtWidgets

from pyftdi.ftdi import Ftdi

from commdefs import *
from stackshot_controller import StackShotController

from gui import GUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())

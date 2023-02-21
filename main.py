import sys
import time
from PySide6 import QtWidgets

from pyftdi.ftdi import Ftdi

from commdefs import *
from stackshot_controller import StackShotController

from main_window import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

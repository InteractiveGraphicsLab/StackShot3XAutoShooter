from PyQt6 import QtWidgets

from Ui_MainWindow import Ui_MainWindow

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

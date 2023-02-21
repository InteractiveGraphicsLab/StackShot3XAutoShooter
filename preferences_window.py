from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_PreferencesWindow import Ui_PreferencesWindow

class PreferencesWindow(QtWidgets.QWidget):
    def __init__(self):
        super(PreferencesWindow, self).__init__()
        self.preferences_window = Ui_PreferencesWindow()
        self.preferences_window.setupUi(self)
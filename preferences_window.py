from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_PreferencesWindow import Ui_PreferencesWindow

import configparser

def isValidBrackets(s, min, max):
    try:
        int(s)
    except ValueError:
        return False

    b = int(s)
    if min <= b <= max:
        return True
    else:
        return False

class PreferencesWindow(QtWidgets.QWidget):
    def __init__(self):
        super(PreferencesWindow, self).__init__()
        self.preferences_window = Ui_PreferencesWindow()
        self.preferences_window.setupUi(self)

        self.preferences_window.imageSrcFolderReferenceButton.clicked.connect(self.getImageSrcFolder)
        self.preferences_window.imageSaveFolderReferenceButton.clicked.connect(self.getImageSaveFolder)
        self.preferences_window.heliconFocusCommandPathReferenceButton.clicked.connect(self.getHeliconFocusCommandPath)

        self.preferences_window.updateConfig.accepted.connect(self.updateConfig)
        self.preferences_window.updateConfig.rejected.connect(self.cancelUpdateConfig)

        self.config = configparser.ConfigParser()
        self.loadConfig()

    def loadConfig(self):
        self.config.read('config.ini')
        # general/brackets
        if 'brackets' in self.config['general'] and \
            isValidBrackets(self.config['general']['brackets'], \
                            self.preferences_window.bracketsSpinBox.minimum(), \
                            self.preferences_window.bracketsSpinBox.maximum()) == True:
            self.preferences_window.bracketsSpinBox.setValue(int(self.config['general']['brackets']))
        else:
            self.preferences_window.bracketsSpinBox.setValue(self.preferences_window.bracketsSpinBox.minimum())
            self.config['general']['brackets'] = str(self.preferences_window.bracketsSpinBox.minimum())
            f = open('config.ini', 'w')
            self.config.write(f)
            f.close()

        # general/image_src_folder
        if 'image_src_folder' in self.config['general'] and 0 < len(self.config['general']['image_src_folder']):
            self.preferences_window.imageSrcFolderPath.setText(self.config['general']['image_src_folder'])
        else:
            self.preferences_window.imageSrcFolderPath.setText('Not selected.')

        # general/image_save_folder
        if 'image_save_folder' in self.config['general'] and 0 < len(self.config['general']['image_save_folder']):
            self.preferences_window.imageSaveFolderPath.setText(self.config['general']['image_save_folder'])
        else:
            self.preferences_window.imageSaveFolderPath.setText('Not selected.')

        # heliconfocus/heliconfocus_command_path
        if 'heliconfocus_command_path' in self.config['heliconfocus'] and 0 < len(self.config['heliconfocus']['heliconfocus_command_path']):
            self.preferences_window.heliconfocusCommandPath.setText(self.config['heliconfocus']['heliconfocus_command_path'])
        else:
            self.preferences_window.heliconfocusCommandPath.setText('Not selected.')

    def updateConfig(self):
        self.config['general']['brackets'] = str(self.preferences_window.bracketsSpinBox.value())
        if self.preferences_window.imageSrcFolderPath.text() != 'Not selected.':
            self.config['general']['image_src_folder'] = self.preferences_window.imageSrcFolderPath.text()
        if self.preferences_window.imageSaveFolderPath.text() != 'Not selected.':
            self.config['general']['image_save_folder'] = self.preferences_window.imageSaveFolderPath.text()
        if self.preferences_window.heliconfocusCommandPath.text() != 'Not selected.':
            self.config['heliconfocus']['heliconfocus_command_path'] = self.preferences_window.heliconfocusCommandPath.text()

        f = open('config.ini', 'w')
        self.config.write(f)
        f.close()
        self.close()

    def cancelUpdateConfig(self):
        self.loadConfig()
        self.close()

    def getImageSrcFolder(self):
        file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(file) != 0:
            self.preferences_window.imageSrcFolderPath.setText(file)

    def getImageSaveFolder(self):
        file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(file) != 0:
            self.preferences_window.imageSaveFolderPath.setText(file)

    def getHeliconFocusCommandPath(self):
        file, check = QtWidgets.QFileDialog.getOpenFileUrl()
        if check:
            self.preferences_window.heliconfocusCommandPath.setText(file.url())

from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_MainWindow import Ui_MainWindow

import os
import usb.core
import subprocess
import configparser

from PySide6 import QtGui
from threading import Thread
from multiprocessing import Value 
from commdefs import *
from stackshot_controller import StackShotController
from action_parser import action_parser
from exec_actions import exec_actions


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


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.startButton.clicked.connect(self.start)
        self.gui.stopButton.clicked.connect(self.stop)

        self.gui.saveActionButton.clicked.connect(self.saveAction)
        self.gui.loadActionButton.clicked.connect(self.loadAction)

        self.gui.imageSrcFolderReferenceButton.clicked.connect(self.updateImageSrcFolder)
        self.gui.imageSaveFolderReferenceButton.clicked.connect(self.updateImageSaveFolder)
        self.gui.metashapeProjectFolderPathReferenceButton.clicked.connect(self.updateMetashapeProjectFolder)

        self.config = configparser.ConfigParser()
        self.loadConfig()

        self.working_thread = None
        self.stop_flag = Value('i', 0) # 0: false, 1: true

        self.controller = StackShotController()
        try:
            print('connecting to Stackshot3X...')
            self.controller.open()
        except Exception as excpt:
            print(excpt)
            exit()


    def loadConfig(self):
        self.config.read('config.ini')
        if not 'general' in self.config:
            self.config['general'] = {}
        # general/brackets
        if 'brackets' in self.config['general'] and \
            isValidBrackets(self.config['general']['brackets'], \
                            self.gui.brackets.minimum(), self.gui.brackets.maximum()) == True:
            self.gui.brackets.setValue(int(self.config['general']['brackets']))
        else:
            self.gui.brackets.setValue(self.gui.brackets.minimum())
            self.config['general']['brackets'] = str(self.gui.brackets.minimum())
            f = open('config.ini', 'w')
            self.config.write(f)
            f.close()

        # general/image_src_folder
        if 'image_src_folder' in self.config['general'] and 0 < len(self.config['general']['image_src_folder']):
            self.gui.imageSrcFolderPath.setText(self.config['general']['image_src_folder'])
        else:
            self.gui.imageSrcFolderPath.setText('Not selected.')

        # general/image_save_folder
        if 'image_save_folder' in self.config['general'] and 0 < len(self.config['general']['image_save_folder']):
            self.gui.imageSaveFolderPath.setText(self.config['general']['image_save_folder'])
        else:
            self.gui.imageSaveFolderPath.setText('Not selected.')

        # general/metashape_project_folder
        if 'metashape_project_folder' in self.config['general'] and 0 < len(self.config['general']['metashape_project_folder']):
            self.gui.metashapeProjectFolderPath.setText(self.config['general']['metashape_project_folder'])
        else:
            self.gui.metashapeProjectFolderPath.setText('Not selected.')

    def updateImageSrcFolder(self):
        file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(file) != 0:
            self.gui.imageSrcFolderPath.setText(file)
            self.config['general']['image_src_folder'] = self.gui.imageSrcFolderPath.text()
            f = open('config.ini', 'w')
            self.config.write(f)
            f.close()

    def updateImageSaveFolder(self):
        file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(file) != 0:
            self.gui.imageSaveFolderPath.setText(file)
            self.config['general']['image_save_folder'] = self.gui.imageSaveFolderPath.text()
            f = open('config.ini', 'w')
            self.config.write(f)
            f.close()

    def updateMetashapeProjectFolder(self):
        file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(file) != 0:
            self.gui.metashapeProjectFolderPath.setText(file)
            self.config['general']['metashape_project_folder'] = self.gui.metashapeProjectFolderPath.text()
            f = open('config.ini', 'w')
            self.config.write(f)
            f.close()

    def loadAction(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', '.', "Text file (*.txt)")
        if fname[0]:
            f = open(fname[0], 'r')
            actions = f.read()
            f.close()
            self.gui.actionsPanel.setPlainText(actions)

    def saveAction(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save As', '.', "Text file (*.txt)")
        if fname[0]:
            f = open(fname[0], 'w')
            f.write(self.gui.actionsPanel.toPlainText())
            f.close()

    def start(self):
        print('start')
        with self.stop_flag.get_lock():
            self.stop_flag.value = 0 # false
        self.working_thread = Thread(target=exec_actions, args=(self.stop_flag, self.gui.actionsPanel.toPlainText(), self.controller, self.gui.brackets.value(), self.gui.doFocusStacking.isChecked(), self.gui.doMetashape.isChecked(), self.config), daemon=True)
        self.working_thread.start()

    def stop(self):
        if self.working_thread != None and self.working_thread.is_alive():
            print('stop')
            with self.stop_flag.get_lock():
                self.stop_flag.value = 1 # true

    def closeEvent(self, event: QtGui.QCloseEvent):
        if self.working_thread != None and self.working_thread.is_alive():
            print('stop')
            with self.stop_flag.get_lock():
                self.stop_flag.value = 1 # true
            self.working_thread.join()
        try:
            print('discoonnecting from Stackshot3X...')
            self.controller.stop(RailAxis.COMM_RAIL_AXIS_X)
            self.controller.stop(RailAxis.COMM_RAIL_AXIS_Y)
            self.controller.stop(RailAxis.COMM_RAIL_AXIS_Z)
            self.controller.close()
        except Exception as excpt:
            print(excpt)
            return

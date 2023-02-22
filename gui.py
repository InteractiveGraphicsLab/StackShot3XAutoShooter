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

from multiprocessing import Process
from commdefs import *
from stackshot_controller import StackShotController
from action_parser import action_parser


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

        self.gui.imageSrcFolderReferenceButton.clicked.connect(self.updateImageSrcFolder)
        self.gui.imageSaveFolderReferenceButton.clicked.connect(self.updateImageSaveFolder)
        self.gui.metashapeProjectFolderPathReferenceButton.clicked.connect(self.updateMetashapeProjectFolder)

        self.config = configparser.ConfigParser()
        self.loadConfig()

        self.current_process = None

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

    def start(self):
        self.current_process = Process(target=self.exec_action)
        self.current_process.start()
        self.gui.startButton.setEnabled(False)
        self.gui.startButton.setText('running')
        self.current_process.join()
        self.gui.startButton.setEnabled(True)
        self.gui.startButton.setText('start')
        self.current_process = None

    def stop(self):
        if self.current_process != None:
            self.current_process.kill()


    def exec_action(self):
        raw_actions = self.gui.actionsText.toPlainText()
        self.stop_flag = False

        # validation
        try:
            action_queue = action_parser(raw_actions)
            print(action_queue)
        except Exception as e:
                print(e)
                return

        controller = StackShotController()
        try:
            controller.open()
            controller.stop(RailAxis.COMM_RAIL_AXIS_X)
            controller.stop(RailAxis.COMM_RAIL_AXIS_Y)
            controller.stop(RailAxis.COMM_RAIL_AXIS_Z)
        except Exception as excpt:
            print(excpt)
            return

        shutter_count = 0
        tmp_dir = self.gui.imageSrcFolderPath.text() # src folder
        save_basedir = self.gui.imageSaveFolderPath.text() # save folder
        brackets = self.gui.brackets.value() # num of brackets
        # debbug output
        print("tmp dir:", tmp_dir)
        print("save basedir", save_basedir)
        print("brackets:", brackets)
        try:
            for action in action_queue:
                if self.stop_flag == True:
                    return

                if action[0] == 'move':
                    if action[1] == 'x':
                        controller.move(RailAxis.COMM_RAIL_AXIS_X, RailDir.COMM_RAIL_DIR_FWD, float(action[2]))
                    elif action[1] == 'y':
                        controller.move(RailAxis.COMM_RAIL_AXIS_Y, RailDir.COMM_RAIL_DIR_FWD, float(action[2]))
                    elif action[1] == 'z':
                        controller.move(RailAxis.COMM_RAIL_AXIS_Z, RailDir.COMM_RAIL_DIR_FWD, float(action[2]))

                elif action[0] == 'shutter':
                    controller.shutter(1, 1., 2.) # NOTE

                    image_paths = [os.path.join(tmp_dir, f) for f in os.listdir(tmp_dir)] # NOTE need ext check
                    image_paths.sort(key=os.path.getmtime, reverse=True) # desc images timestamp
                    save_image_paths = image_paths[:brackets]

                    save_dir = os.path.join(save_basedir, 'original', str(shutter_count).zfill(4)) # image save dir
                    os.makedirs(save_dir) # create image save dir
                    for image_path in save_image_paths:
                        image_name = os.path.basename(image_path)
                        os.rename(image_path, os.path.join(save_dir, image_name)) # move image
                    shutter_count += 1

        except Exception as excpt:
            print(excpt)

        finally:
            controller.close()

        if self.gui.doFocusStacking.isChecked() == True:
            # focus stacking
            original_images_dirs = os.listdir(os.path.join(save_basedir, 'original'))
            os.makedirs(os.path.join(save_basedir, 'stacking')) # create stacking images dir
            try:
                for original_dir in original_images_dirs:
                    if self.stop_flag == True:
                        return

                    subprocess.run([self.config['general']['heliconfocus_command_path'], \
                                    '-silent', \
                                    os.path.join(save_basedir, 'original', original_dir), \
                                    '-save:' + os.path.join(save_basedir, 'stacking', original_dir + '.jpg'), \
                                    '-mp:2', \
                                    '-j:100'], check=True)
            except Exception as excpt :
                print(excpt)

        if self.gui.doMetashape.isChecked() == True:
            # metashape
            env = os.environ
            env['IMAGE_PATH'] = os.path.join(save_basedir, 'stacking')
            env['METASHAPE_PROJECT_PATH'] = self.gui.metashapeProjectFolderPath.text()
            subprocess.run([self.config['general']['metashape_command_path'], '--gui', '-r', 'metashape_script.py'], env=env)

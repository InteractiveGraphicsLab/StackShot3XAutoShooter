from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_MainWindow import Ui_MainWindow
from preferences_window import PreferencesWindow

import os
import usb.core
import subprocess

from commdefs import *
from stackshot_controller import StackShotController
from action_parser import action_parser


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        self.main_window.startButton.clicked.connect(self.start)

        self.main_window.doFocusStacking.stateChanged.connect(self.clickDoFocusStackingCheckbox)
        self.main_window.doMetashape.stateChanged.connect(self.clickDoMetashapeCheckbox)

        self.main_window.actionPreference.triggered.connect(self.showPreferences)

        self.preferences_window = PreferencesWindow()

    def clickDoFocusStackingCheckbox(self):
        self.main_window.heliconFocusCommandPathLabel.setVisible(not self.main_window.heliconFocusCommandPathLabel.isVisible())
        self.main_window.heliconFocusCommandPath.setVisible(not self.main_window.heliconFocusCommandPath.isVisible())

    def clickDoMetashapeCheckbox(self):
        self.main_window.metashapeCommandPathLabel.setVisible(not self.main_window.metashapeCommandPathLabel.isVisible())
        self.main_window.metashapeCommandPath.setVisible(not self.main_window.metashapeCommandPath.isVisible())
        self.main_window.metashapeProjectPathLabel.setVisible(not self.main_window.metashapeProjectPathLabel.isVisible())
        self.main_window.metashapeProjectPath.setVisible(not self.main_window.metashapeProjectPath.isVisible())

    def showPreferences(self):
        self.preferences_window.show()

    # def start(rawComands: str):
    def start(self):
        raw_actions = self.main_window.actionsText.toPlainText()

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
        tmp_dir = self.main_window.imageTmpPath.text() # tmp dir
        save_basedir = self.main_window.imageSavePath.text() # save path
        brackets = self.main_window.brackets.value() # num of brackets
        focus_stacking_cmd_path = self.main_window.heliconFocusCommandPath.text() # focus stacking command path
        # debbug output
        print("tmp dir:", tmp_dir)
        print("save basedir", save_basedir)
        print("brackets:", brackets)
        print("focus stacking cmd path:", focus_stacking_cmd_path)
        try:
            for action in action_queue:
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

        if self.main_window.doFocusStacking.isChecked() == True:
            # focus stacking
            original_images_dirs = os.listdir(os.path.join(save_basedir, 'original'))
            os.makedirs(os.path.join(save_basedir, 'stacking')) # create stacking images dir
            try:
                for original_dir in original_images_dirs:
                    print(original_dir)
                    subprocess.run([focus_stacking_cmd_path, \
                                    '-silent', \
                                    os.path.join(save_basedir, 'original', original_dir), \
                                    '-save:' + os.path.join(save_basedir, 'stacking', original_dir + '.jpg'), \
                                    '-mp:2', \
                                    '-j:100'], check=True)
            except Exception as excpt :
                print(excpt)

        if self.main_window.doMetashape.isChecked() == True:
            # metashape
            env = os.environ
            env['IMAGE_PATH'] = os.path.join(save_basedir, 'stacking')
            env['METASHAPE_PROJECT_PATH'] = self.main_window.metashapeProjectPath.text()
            subprocess.run([self.main_window.metashapeCommandPath.text(), '-r', 'metashape_script.py'], env=env)

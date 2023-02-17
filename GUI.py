from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_Ui_MainWindow import Ui_MainWindow

import os
import usb.core
import subprocess

from commdefs import *
from stackshot_controller import StackShotController
from action_parser import action_parser


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.startButton.clicked.connect(self.start)

        self.gui.doFocusStacking.stateChanged.connect(self.clickDoFocusStackingCheckbox)

    def clickDoFocusStackingCheckbox(self):
        self.gui.heliconFocusCommandPathLabel.setVisible(not self.gui.heliconFocusCommandPathLabel.isVisible())
        self.gui.heliconFocusCommandPath.setVisible(not self.gui.heliconFocusCommandPath.isVisible())

    # def start(rawComands: str):
    def start(self):
        raw_actions = self.gui.actionsText.toPlainText()

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
        tmp_dir = self.gui.imageTmpPath.text() # tmp dir
        save_basedir = self.gui.imageSavePath.text() # save path
        brackets = self.gui.brackets.value() # num of brackets
        focus_stacking_cmd_path = self.gui.heliconFocusCommandPath.text() # focus stacking command path
        # debbug output
        print("tmp dir:", tmp_dir)
        print("save basedir", save_basedir)
        print("brackets:", brackets)
        print("focus stacking cmd path:", focus_stacking_cmd_path)
        try:
            for action in action_queue:
                if action[0] == 'move':
                    if action[1] == 'x':
                        controller.move(RailAxis.COMM_RAIL_AXIS_X, RailDir.COMM_RAIL_DIR_FWD, int(action[2]))
                    elif action[1] == 'y':
                        controller.move(RailAxis.COMM_RAIL_AXIS_Y, RailDir.COMM_RAIL_DIR_FWD, int(action[2]))
                    elif action[1] == 'z':
                        controller.move(RailAxis.COMM_RAIL_AXIS_Z, RailDir.COMM_RAIL_DIR_FWD, int(action[2]))

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
                    print(original_dir)
                    subprocess.run([focus_stacking_cmd_path, \
                                    '-silent', \
                                    os.path.join(save_basedir, 'original', original_dir), \
                                    '-save:' + os.path.join(save_basedir, 'stacking', original_dir + '.jpg'), \
                                    '-mp:2', \
                                    '-j:100'], check=True)
            except Exception as excpt :
                print(excpt)

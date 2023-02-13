from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_Ui_MainWindow import Ui_MainWindow

import os

from commdefs import *
from stackshot_controller import StackShotController
from action_parser import action_parser


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.startButton.clicked.connect(self.start)

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
        except Exception as excpt:
            print(excpt)
            return

        try:
            shutter_count = 0
            tmp_dir = self.gui.imageTmpPath.text() # tmp dir
            save_basedir = self.gui.imageSavePath.text() # save path
            brackets = self.gui.brackets.value() # num of brackets
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
                    brackets = 16 # NOTE get from config??
                    save_image_paths = image_paths[:brackets]

                    save_dir = os.path.join(save_basedir, str(shutter_count).zfill(4)) # image save dir
                    os.makedirs(save_dir) # create image save dir
                    for image_path in save_image_paths:
                        image_name = os.path.basename(image_path)
                        os.rename(image_path, os.path.join(save_dir, image_name)) # move image
                    shutter_count += 1

        except Exception as excpt:
            print(excpt)

        finally:
            controller.close()

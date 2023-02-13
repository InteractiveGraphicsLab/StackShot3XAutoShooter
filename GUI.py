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
        raw_commands = self.gui.plainTextEdit.toPlainText()

        # validation
        try:
            action_queue = action_parser(raw_commands)
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

                    savedir = '' ## 保存先ディレクトリ
                    os.makedirs(savedir) # 保存ディレクトリを作成

                    tmpdir = '' ## 撮影された写真が保存される一時ディレクトリ
                    image_paths = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir)] # NOTE need ext check
                    image_paths.sort(key=os.path.getmtime, reverse=True) # 画像のタイムスタンプの降順
                    brackets = 16 # NOTE get from config??
                    save_image_paths = image_paths[:brackets]

                    for image_path in save_image_paths:
                        image_name = os.path.basename(image_path)
                        os.rename(image_path, os.path.join(savedir, str(shutter_count).zfill(4), image_name)) # ファイル移動
                    shutter_count += 1

        except Exception as excpt:
            print(excpt)

        finally:
            controller.close()

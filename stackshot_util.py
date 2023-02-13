import os

from commdefs import *
from stackshot_controller import StackShotController
from action_parser import action_parser


def start(rawComands: str):
    # validation
    try:
        action_queue = action_parser(rawComands)
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
                images = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir)] # NOTE need ext check
                images.sort(key=os.path.getmtime, reverse=True) # 画像のタイムスタンプの降順
                brackets = 16 # NOTE get from config??
                save_images = images[:brackets]

                for image in save_images:
                    os.rename(os.path.join(tmpdir, image), os.path.join(savedir, image)) # ファイル移動

    except Exception as excpt:
        print(excpt)

    finally:
        controller.close()

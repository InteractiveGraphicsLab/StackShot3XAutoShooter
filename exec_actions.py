import os
import signal
import subprocess

from commdefs import *
from action_parser import action_parser
from stackshot_controller import StackShotController


def exec_actions(stop_flag, raw_actions, controller, brackets, doFocusStacking, doMetashape, config):
    # validation
    try:
        action_queue = action_parser(raw_actions)
        print(action_queue)
    except Exception as e:
            print(e)
            return

    shutter_count = 0
    tmp_dir = config['general']['image_src_folder'] # src folder
    save_basedir = config['general']['image_save_folder'] # save folder
    # debbug output
    print("tmp dir:", tmp_dir)
    print("save basedir", save_basedir)
    print("brackets:", brackets)
    try:
        controller.stop(RailAxis.COMM_RAIL_AXIS_X)
        controller.stop(RailAxis.COMM_RAIL_AXIS_Y)
        controller.stop(RailAxis.COMM_RAIL_AXIS_Z)

        for action in action_queue:
            with stop_flag.get_lock():
                if stop_flag.value == 1: # true
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

    if doFocusStacking == True:
        # focus stacking
        original_images_dirs = os.listdir(os.path.join(save_basedir, 'original'))
        os.makedirs(os.path.join(save_basedir, 'stacking')) # create stacking images dir
        try:
            for original_dir in original_images_dirs:
                with stop_flag.get_lock():
                    if stop_flag.value == 1: # true
                        return
                subprocess.run([config['general']['heliconfocus_command_path'], \
                                '-silent', \
                                os.path.join(save_basedir, 'original', original_dir), \
                                '-save:' + os.path.join(save_basedir, 'stacking', original_dir + '.jpg'), \
                                '-mp:2', \
                                '-j:100'], check=True)
        except Exception as excpt :
            print(excpt)

    if doMetashape == True:
        # metashape
        env = os.environ
        env['IMAGE_PATH'] = os.path.join(save_basedir, 'stacking')
        env['METASHAPE_PROJECT_PATH'] = config['general']['metashape_project_folder']
        subprocess.run([config['general']['metashape_command_path'], '--gui', '-r', 'metashape_script.py'], env=env)

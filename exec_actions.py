import os
import time
import signal
import subprocess

from StackShot3X_API_for_Python.commdefs import *
from action_parser import action_parser
from StackShot3X_API_for_Python.stackshot_controller import StackShotController

def exec_actions(stop_flag, raw_actions: str, controller: StackShotController, brackets: int, doFocusStacking: bool, doMetashape: bool, config):
    # validation and parse actions
    try:
        action_queue = action_parser(raw_actions)
    except Exception as e:
            print(e)
            return

    shutter_count = 0
    image_src_folder = config['general']['image_src_folder']
    image_save_folder = config['general']['image_save_folder']

    # debbug output
    print("image src folder:", image_src_folder)
    print("image save folder:", image_save_folder)
    if doFocusStacking:
        print("brackets:", brackets)
    if doMetashape:
        print("metashape project folder:", config['general']['metashape_project_folder'])

    try:
        # send stop command in advance to prevent infinite move, 
        controller.stop(RailAxis.X)
        controller.stop(RailAxis.Y)
        controller.stop(RailAxis.Z)

        # execute all actions
        for action in action_queue:
            # check if stop_flag is true
            with stop_flag.get_lock():
                if stop_flag.value == 1: # true
                    return

            # move axis
            if action[0] == 'move':
                axis = None
                if action[1] == 'x':
                    axis = RailAxis.X
                elif action[1] == 'y':
                    axis = RailAxis.Y
                elif action[1] == 'z':
                    axis = RailAxis.Z

                controller.move(axis, RailDir.FWD, float(action[2]))

                # wait for rail stop
                while controller.get_status(axis) != RailStatus.IDLE:
                    time.sleep(0.2)


            # shoot camera
            elif action[0] == 'shutter':
                controller.shutter(1, 1., 2.) # NOTE

                # wait for finish shutter
                while controller.get_status(RailAxis.ANY) != RailStatus.IDLE:
                    time.sleep(0.2)

                image_paths = [os.path.join(image_src_folder, f) for f in os.listdir(image_src_folder)]
                image_paths.sort(key=os.path.getmtime, reverse=True) # desc images timestamp
                save_image_paths = image_paths[:brackets]

                save_dir = os.path.join(image_save_folder, 'original', str(shutter_count).zfill(4)) # image save dir
                os.makedirs(save_dir) # create image save dir
                for image_path in save_image_paths:
                    image_name = os.path.basename(image_path)
                    os.rename(image_path, os.path.join(save_dir, image_name)) # move image
                shutter_count += 1

    except Exception as excpt:
        print(excpt)

    if doFocusStacking == True:
        # focus stacking
        original_images_dirs = os.listdir(os.path.join(image_save_folder, 'original'))
        os.makedirs(os.path.join(image_save_folder, 'stacking')) # create stacking images dir
        try:
            # focus stacking on each view
            for original_dir in original_images_dirs:
                with stop_flag.get_lock():
                    if stop_flag.value == 1: # true
                        return
                # run heliconfocus 
                subprocess.run([config['general']['heliconfocus_command_path'], \
                                '-silent', \
                                os.path.join(image_save_folder, 'original', original_dir), \
                                '-save:' + os.path.join(image_save_folder, 'stacking', original_dir + '.jpg'), \
                                '-mp:2', \
                                '-j:100'], check=True)
        except Exception as excpt :
            print(excpt)

    if doMetashape == True:
        # path image-path and metashape-project-path by enviroment variable
        env = os.environ
        env['IMAGE_PATH'] = os.path.join(image_save_folder, 'stacking')
        env['METASHAPE_PROJECT_PATH'] = config['general']['metashape_project_folder']

        # run metashape
        subprocess.run([config['general']['metashape_command_path'], '--gui', '-r', 'metashape_script.py'], env=env)

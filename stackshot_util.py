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

    try:
        controller = StackShotController()
        controller.open()

        for action in action_queue:
            if action[0] == 'move':
                if action[1] == 'x':
                    controller.move(RailAxis.COMM_RAIL_AXIS_X, RailDir.COMM_RAIL_DIR_FWD, int(action[2]))
                elif action[1] == 'y':
                    controller.move(RailAxis.COMM_RAIL_AXIS_Y, RailDir.COMM_RAIL_DIR_FWD, int(action[2]))
                elif action[1] == 'z':
                    controller.move(RailAxis.COMM_RAIL_AXIS_Z, RailDir.COMM_RAIL_DIR_FWD, int(action[2]))

    except Exception as excpt:
        print(excpt)

    finally:
        controller.close()

def shutter():
    try:
        controller = StackShotController()
        controller.open()

        controller.shutter(1, 1., 2.) # NOTE

    except Exception as excpt:
        print(excpt)

    finally:
        controller.close()

from commdefs import *
from stackshot_controller import StackShotController


def start(rawComands: str):
    commands = []
    for line in rawComands.splitlines():
        commands.append(line.split())

    # validation

    try:
        controller = StackShotController()
        controller.open()

        for cmd in commands:
            if cmd[0] == 'MOVE':
                if cmd[1] == 'X':
                    controller.move(RailAxis.COMM_RAIL_AXIS_X, RailDir.COMM_RAIL_DIR_FWD, int(cmd[2]))
                elif cmd[1] == 'Y':
                    controller.move(RailAxis.COMM_RAIL_AXIS_Y, RailDir.COMM_RAIL_DIR_FWD, int(cmd[2]))
                elif cmd[1] == 'Z':
                    controller.move(RailAxis.COMM_RAIL_AXIS_Z, RailDir.COMM_RAIL_DIR_FWD, int(cmd[2]))

    except Exception as excpt:
        print(excpt)

    finally:
        controller.close()

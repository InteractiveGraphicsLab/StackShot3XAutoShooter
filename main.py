import time
from pyftdi.ftdi import Ftdi

from commdefs import *
from stackshot_controller import StackShotController

if __name__ == '__main__':
    try:
        controller = StackShotController()
        controller.open()

        dist = 5
        controller.move(RailAxis.COMM_RAIL_AXIS_Z, RailDir.COMM_RAIL_DIR_FWD, dist)
        controller.move(RailAxis.COMM_RAIL_AXIS_X, RailDir.COMM_RAIL_DIR_FWD, dist)

        controller.move(RailAxis.COMM_RAIL_AXIS_Z, RailDir.COMM_RAIL_DIR_BACK, dist)
        controller.move(RailAxis.COMM_RAIL_AXIS_X, RailDir.COMM_RAIL_DIR_BACK, dist)

    except Exception as excpt:
        print(excpt)

    finally:
        controller.close()

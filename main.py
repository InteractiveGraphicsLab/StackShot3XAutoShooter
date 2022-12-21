import time
from pyftdi.ftdi import Ftdi

from stackshot_api import *

def main(device: Ftdi):
    try:
        dist = 5

        stackshot_move(device, CommRailAxis.COMM_RAIL_AXIS_X, CommRailDir.COMM_RAIL_DIR_FWD, CommRailUnits.COMM_RAIL_UNITS_METRIC, True, dist)

        stackshot_move(device, CommRailAxis.COMM_RAIL_AXIS_Y, CommRailDir.COMM_RAIL_DIR_FWD, CommRailUnits.COMM_RAIL_UNITS_METRIC, True, dist)

    except Exception as e:
        print('\n', 'Exception:', e, '\n')

if __name__ == '__main__':
    try:
        device = stackshot_open('ftdi://ftdi:232:AI04PHAW/1')
        main(device)

    except Exception as excpt:
        print(excpt)

    finally:
        stackshot_close(device)

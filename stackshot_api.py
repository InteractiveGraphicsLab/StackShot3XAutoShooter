import time
import ctypes

from commdefs import *
from pyftdi.ftdi import Ftdi


"""
Form1(void)
{
    InitializeComponent();

    this->configSelection->SelectedIndex = 0;
    this->railDirection->SelectedIndex = 0;
    this->railUnits->SelectedIndex = 1;
    this->railBacklash->SelectedIndex = 1;
    this->moveAxis->SelectedIndex = 0;
}
"""


def send_command(device: Ftdi, axis: CommRailAxis, cmd: CommCmd, action: CommAction, data: bytearray | None, lenIn: int):
    cmd = int(cmd)
    print(axis)
    action = (int(action) | (int(axis-1) << 4))

    byte = bytearray()
    byte.extend(b'\x55')
    byte.extend(((cmd >> 8) & 0x0FF).to_bytes(1, 'big'))
    byte.extend(( cmd       & 0x0FF).to_bytes(1, 'big'))
    byte.extend((action & 0x0FF).to_bytes(1, 'big'))
    byte.extend(lenIn.to_bytes(1, 'big')) # CMD length
    if data != None:
        for d in data:
            byte.extend(d.to_bytes(1, 'big'))
    byte.extend(b'\x69') # checksum
    # print(byte)

    n = device.write_data(byte)
    time.sleep(1)
    # print(n)

    ### wait for response
    res = device.read_data(100)
    time.sleep(1) # ??

    """
    Format of received data:
    buffer[0] = 0xAA (Ack)
    buffer[1] = cmd High
    buffer[2] = cmd Low
    buffer[3] = action
    buffer[4] = Length of data
    buffer[5] = data......
    buffer[n] = checksum;
    """
    # res_cmd = res[1] << 8 | res[2]
    # print('res_cmd:', CommCmd(res_cmd))

    res_response = res[3]
    if res_response != int(CommAction.COMM_ACTION_RSP_OK):
        print('response:', res_response.to_bytes(1, 'big'))

    res_buffsize = res[4]
    # print('res_buffsize:', res_buffsize)

    res_data = None
    if 0 < res_buffsize:
        res_data = bytearray()
        for i in range(5, 5+res_buffsize):
            res_data.extend(res[i].to_bytes(1, 'big'))

    return res_data


def stackshot_open(url: str):
    print("=== Open ===")
    device = Ftdi()
    device.open_from_url(url)

    device.set_bitmode(0xFF, Ftdi.BitMode.CBUS)

    time.sleep(0.5)

    device.set_baudrate(STACKSHOT_BAUD_RATE)
    device.set_flowctrl('') # no flow controll

    return device


def stackshot_close(device: Ftdi):
    print('\n=== Close ===')
    device.set_bitmode(0xF0, Ftdi.BitMode.CBUS)
    send_command(device,
                 CommRailAxis.COMM_RAIL_AXIS_ANY,
                 CommCmd.CC_CLOSE,
                 CommAction.COMM_ACTION_WRITE,
                 None,
                 0)
    device.close()


# NOTE axis不要?
def stackshot_get_nvmregister(device: Ftdi, axis: CommRailAxis, reg: int):
    data = bytearray()
    data.extend(reg.to_bytes(1, 'big'))

    res_data = send_command(device,
                            axis,
                            CommAction.COMM_ACTION_READ,
                            data,
                            1)
    reg_data = int(res_data[1]) | (int(res_data[2]) << 8) | (int(res_data[3]) << 16) | (int(res_data[4]) << 24)

    return reg_data


# NOTE axis不要?
def stackshot_set_nvmregister(device: Ftdi, axis, reg: int, regData: int):
    data = bytearray()
    data.extend(reg.to_bytes(1, 'big'))
    data.extend((regData & 0x0FF).to_bytes(1, 'big'))
    data.extend(((regData >>  8) & 0x0FF).to_bytes(1, 'big'))
    data.extend(((regData >> 16) & 0x0FF).to_bytes(1, 'big'))
    data.extend(((regData >> 24) & 0x0FF).to_bytes(1, 'big'))

    send_command(device,
                 axis,
                 CommCmd.CC_NVM_ACCESS,
                 CommAction.COMM_ACTION_WRITE,
                 data,
                 5)


def stackshot_get_axis(device: Ftdi):
    print('\n=== GetAxis ===')
    axis = stackshot_get_nvmregister(device, CommRailAxis.COMM_RAIL_AXIS_ANY, 0)
    return CommRailAxis(axis)


def stackshot_set_axis(device: Ftdi, axis: CommRailAxis):
    print('\n=== SetAxis ===')
    stackshot_set_nvmregister(device, axis, 0, int(axis))


def stackshot_get_status(device: Ftdi, axis: CommRailAxis):
    print('\n=== GetStatus ===')
    res = send_command(device, axis, CommCmd.CC_RAIL_STATUS, CommAction.COMM_ACTION_READ, None, 0)
    status = (int(res[0])) | (int(res[1]) << 8) | (int(res[2]) << 16) | (int(res[3]) << 24)

    return status


def stackshot_move(device: Ftdi, axis: CommRailAxis, dir: CommRailDir, units: CommRailUnits, backlash: bool, dist: float):
    print('\n=== Move ===')

    # castedDistPtr = (unsigned int*)&dist
    distPtr = ctypes.pointer(ctypes.c_float(dist))
    castedDistPtr = ctypes.cast(distPtr, ctypes.POINTER(ctypes.c_uint))
    castedDist = castedDistPtr.contents.value

    data = bytearray()
    data.extend(int(dir).to_bytes(1, 'big'))
    data.extend(int(units).to_bytes(1, 'big'))
    data.extend(backlash.to_bytes(1, 'big'))
    data.extend(( castedDist        & 0x0FF).to_bytes(1, 'big'))
    data.extend(((castedDist >>  8) & 0x0FF).to_bytes(1, 'big'))
    data.extend(((castedDist >> 16) & 0x0FF).to_bytes(1, 'big'))
    data.extend(((castedDist >> 24) & 0x0FF).to_bytes(1, 'big'))

    send_command(device, axis, CommCmd.CC_RAIL_MOVE, CommAction.COMM_ACTION_WRITE, data, 7)

    while(True):
        if stackshot_get_status(device, axis) != RAIL_STATUS_MOVING:
            break
        time.sleep(0.5)

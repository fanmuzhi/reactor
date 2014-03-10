#!/usr/bin/env python
# encoding: utf-8

"""test the 128 DUTs switch.

TCA9555 to control the relay:
    Address: 0x20 + channel number
    Command Byte:
        input = 0x00
        output = 0x02
        config = 0x06

    Relay matrix: (B for dischage, A for charge)
        bit: 4B 4A 3B 3A 2B 2A 1B 1A
        sta:  1  1  1  1  1  1  1  1
        bit: 8B 8A 7B 7A 6B 6A 5B 5A
        sta:  1  1  1  1  1  1  1  1

"""

from topaz.i2c_adapter import DeviceAPI

REG_OUTPUT = 0x02
REG_CONFIG = 0x06


def charge_relay(chnum, slotnum, open=True):
    global_da.slave_addr = 0x20  # 0100000

    # config PIO to output
    wdata = [REG_CONFIG, 0x00, 0x00]
    global_da.write(wdata)

    # set charge relay
    wdata = [REG_OUTPUT, 0x01, 0x40]
    global_da.write(wdata)


def discharge_relay(dutnum, open=True):
    global_da.slave_addr = 0x20  # 0100000

    # config PIO to output
    wdata = [REG_CONFIG, 0x00, 0x00]
    global_da.write(wdata)

    # set charge relay
    wdata = [REG_OUTPUT, 0x02, 0x80]
    global_da.write(wdata)


if __name__ == "__main__":
    # init
    global_da = DeviceAPI(bitrate=400)
    global_da.open(portnum=0)

    import time
    charge_relay(0, 1)
    #time.sleep(30)
    #discharge_relay(1)

    # close
    global_da.close()

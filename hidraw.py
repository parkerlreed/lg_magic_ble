#!/usr/bin/env python
import sys
import struct
import uinput
import subprocess

last_btn = None

device = uinput.Device([
        uinput.KEY_1,
        uinput.KEY_2,
        uinput.KEY_3,
        uinput.KEY_4,
        uinput.KEY_5,
        uinput.KEY_6,
        uinput.KEY_7,
        uinput.KEY_8,
        uinput.KEY_9,
        uinput.KEY_0,
        uinput.KEY_ENTER,
        uinput.KEY_UP,
        uinput.KEY_DOWN,
        uinput.KEY_LEFT,
        uinput.KEY_RIGHT,
        uinput.KEY_ESC,
        uinput.KEY_MUTE,
        uinput.KEY_VOLUMEUP,
        uinput.KEY_VOLUMEDOWN,
        uinput.KEY_PAGEUP,
        uinput.KEY_PAGEDOWN,
        uinput.KEY_HOME,
        uinput.KEY_SCROLLUP,
        uinput.KEY_SCROLLDOWN,
        ])

def bar(val, l=20):
    return ("%02.2f " % (val / 2**9,)).rjust(8) + (
        "#" * int((val + 2**15) / 2**16 * l)
    ).ljust(l)


with open(sys.argv[1], "rb") as fd:
    while True:
        pkt_type = fd.read(1)

        if not pkt_type:
            # EOF
            break

        if pkt_type == b"\xfd":
            # ...read the rest
            chunk = fd.read(19)
            (
                unk1,
                cnt,
                gyro1,
                gyro2,
                gyro3,
                acc1,
                acc2,
                acc3,
                btn_pressed,
                btn_code,
                wheel,
            ) = struct.unpack(">BBxxhhhhhhBBB", chunk)
            if not (last_btn is btn_code) or ((btn_pressed == 128) and (btn_code == 0)):
                match btn_code:
                    case 16:
                        device.emit_click(uinput.KEY_0)
                    case 17:
                        device.emit_click(uinput.KEY_1)
                    case 18:
                        device.emit_click(uinput.KEY_2)
                    case 19:
                        device.emit_click(uinput.KEY_3)
                    case 20:
                        device.emit_click(uinput.KEY_4)
                    case 21:
                        device.emit_click(uinput.KEY_5)
                    case 22:
                        device.emit_click(uinput.KEY_6)
                    case 23:
                        device.emit_click(uinput.KEY_7)
                    case 24:
                        device.emit_click(uinput.KEY_8)
                    case 25:
                        device.emit_click(uinput.KEY_9)
                    case 2:
                        device.emit_click(uinput.KEY_VOLUMEUP)
                    case 3:
                        device.emit_click(uinput.KEY_VOLUMEDOWN)
                    #case 0: Causing issues even with trying to account for it above. Every key release triggers this case.
                    #    device.emit_click(uinput.KEY_PAGEUP)
                    case 1:
                        device.emit_click(uinput.KEY_PAGEDOWN)
                    case 9:
                        device.emit_click(uinput.KEY_MUTE)
                    case 124:
                        device.emit_click(uinput.KEY_HOME)
                    case 64:
                        device.emit_click(uinput.KEY_UP)
                    case 65:
                        device.emit_click(uinput.KEY_DOWN)
                    case 7:
                        device.emit_click(uinput.KEY_LEFT)
                    case 6:
                        device.emit_click(uinput.KEY_RIGHT)
                    case 40:
                        device.emit_click(uinput.KEY_ESC)

                last_btn = btn_code
            match wheel:
                case 1:
                    subprocess.Popen(['xdotool', 'click', '4'])
                case 255:
                    subprocess.Popen(['xdotool', 'click', '5'])
        else:
            print("Unknown packet type:", pkt_type)















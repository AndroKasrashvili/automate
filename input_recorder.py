from abc import ABC

import pyglet
from sys import stdout
from pyglet.window import Window
import time
from json_handler import MyJSONEncoder
from command import Command
from schedule import Schedule
import json
import constants
import argparse


class MyWindow(Window):
    def __init__(self, width, height, name, file_buff):
        super().__init__(width=width, height=height, caption=name)
        self.events = []
        self.buff = file_buff
        self.is_first = True

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.events.append(Schedule(time.clock_gettime(time.CLOCK_MONOTONIC_RAW),
                                    constants.TouchType.DOWN.value, x, y))

    def on_draw(self):
        self.clear()

    def on_mouse_press(self, x, y, button, modifiers):
        self.events.append(Schedule(time.clock_gettime(time.CLOCK_MONOTONIC_RAW),
                                    constants.TouchType.DOWN.value, x, y))

    def on_mouse_release(self, x, y, button, modifiers):
        self.events.append(
            Schedule(time.clock_gettime(time.CLOCK_MONOTONIC_RAW),
                     constants.TouchType.UP.value, x, y))

        cmd = Command(
            constants.CommandType.COMMAND.value,
            constants.CommandId.SYNTHESIZE_TOUCH_INPUT.value,
            self.events
        )
        cmd_json_string = json.dumps(cmd, cls=MyJSONEncoder)
        if self.is_first:
            self.is_first = False
        else:
            self.buff.write(',\n')

        self.buff.write(cmd_json_string)
        self.events = []

    def on_close(self):
        self.buff.write("]")
        self.buff.close()
        super().on_close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get destination file")
    parser.add_argument('-o', nargs=1, type=argparse.FileType('w+'),
                        default=stdout)
    args = parser.parse_args()
    output = args.o[0]
    output.write("[")
    win = MyWindow(width=800, height=600, name='window', file_buff=args.o[0])
    pyglet.app.run()


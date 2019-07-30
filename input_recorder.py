import pyglet
from sys import stdout
from pyglet.window import Window
import time
from JSONHandler import MyJSONEncoder
from Command import Command
from Schedule import Schedule
import json
import constants
import argparse


class MyWindow(Window):
    def __init__(self, width, height, name, fileBuff):
        super().__init__(width=width, height=height, caption=name)
        self.events = []
        self.buff = fileBuff

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
        cmd_json_string = json.dumps(MyJSONEncoder().encode(cmd))
        self.buff.write(cmd_json_string[1:len(cmd_json_string) - 1])
        self.events = []

    def on_close(self):
        self.buff.write("]}\"")
        self.buff.close()
        super().on_close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get destination file")
    parser.add_argument('-o', nargs=1, type=argparse.FileType('w+'),
                        default=stdout)
    args = parser.parse_args()
    output = args.o[0]
    output.write("\"{commands: [")
    win = MyWindow(width=800, height=600, name='window', fileBuff=args.o[0])
    pyglet.app.run()


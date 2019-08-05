import argparse
from sys import stdin
import json
from pyglet.window import Window
import pyglet

from command import Command


class TrackerWindow(Window):
    def __init__(self, width, height, name, points, point_count):
        super().__init__(width=width, height=height, caption=name)
        self.points = points
        self.pointCount = point_count

    def on_draw(self):
        self.clear()
        pyglet.graphics.draw(int(len(self.points)/2), pyglet.gl.GL_POINTS,
                             ('v2i', tuple(self.points))
                             )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get file to read")
    parser.add_argument('-i', nargs=1, type=argparse.FileType('r'),
                        default=stdin)
    args = parser.parse_args()
    input_file = args.i[0]

    commandsDictList = json.load(input_file)
    input_file.close()

    commands = [Command.from_json(com_dict) for com_dict in commandsDictList]

    touches = map(lambda cmd: list(map(lambda schedule: [schedule.x, schedule.y], cmd.touchSchedule)), commands)
    points = sum(list(touches), [])
    win = TrackerWindow(width=800, height=600, name='simulator', points=sum(list(points), []), point_count=len(points))
    pyglet.app.run()




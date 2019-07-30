import argparse
from sys import stdin
import json

from command import Command

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get file to read")
    parser.add_argument('-i', nargs=1, type=argparse.FileType('r'),
                        default=stdin)
    args = parser.parse_args()
    input_file = args.i[0]

    commandsDictList = json.load(input_file)
    input_file.close()

    commands = [Command.from_json(com_dict) for com_dict in commandsDictList]
    print(type(commands[0]))
    print(type(commands[0].touchSchedule[0]))



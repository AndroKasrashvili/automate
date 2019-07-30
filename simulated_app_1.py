import argparse
from sys import stdin

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get file to read")
    parser.add_argument('-i', nargs=1, type=argparse.FileType('r'),
                        default=stdin)
    args = parser.parse_args()
    input_file = args.i[0]
    data = input_file.read()
    print(data)


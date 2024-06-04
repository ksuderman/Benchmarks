import os
import sys

MB = 1024 * 1024
GB = MB * 1024

def run():
    with open('SraRunTable.csv') as f:
        lines = f.read().splitlines(keepends=False)

    for line in lines[1:]:
        parts = line.split(',')
        size = float(parts[7])
        if size > GB:
            value = f"{size / GB:4.1f}GB"
        else:
            value = f"{size / MB:4.1f}MB"

        print(f"{parts[0]},{value}")


if __name__ == "__main__":
    run()
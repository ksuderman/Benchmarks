#!/usr/bin/env python3
import os
import sys


def load_csv_header(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines(keepends=False)
        return lines[0].split(',')


def load_markdown_header(filepath: str):
    with open(filepath) as f:
        lines = f.read().splitlines(keepends=False)
        return lines[0].split('|')[1:-1]


def run(filepath:str):
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    if filepath.endswith('.csv'):
        header = load_csv_header(filepath)
    elif filepath.endswith(".md"):
        header = load_markdown_header(filepath)
    else:
        print(f"ERROR: Unrecognized file type: {filepath}")
        return
    for i in range(0, len(header)):
        print(f"{i:3d}: {header[i]}")


if __name__ == '__main__':
    # parser = ArgumentParser()
    # parser.add_argument('--csv', action='store_true', help='process a CSV file')
    # parser.add_argument('--markdown', action='store_true', help='process a markdown file')

    if len(sys.argv) == 1:
        print(f"USAGE: {sys.argv[0]} <PATH>")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("ERROR: Only one input file is supported")
        sys.exit(1)
    run(sys.argv[1])

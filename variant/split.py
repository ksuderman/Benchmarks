#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser

def run(argv):
    if not os.path.exists(argv.input):
        print(f"ERROR: Input file {argv.input} not found.")
        return
    if not os.path.exists(argv.output):
        print(f"ERROR: Output directory not found")
        return
    if not os.path.isdir(argv.output):
        print(f"ERROR: Output location is not a directory.")
        return



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', help='input file containing paired end reads', required=True)
    parser.add_argument('-o', '--output', help='directory where output files will be written', required=True)
    argv = parser.parse_args(sys.argv[1:])

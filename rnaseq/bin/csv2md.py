#!/usr/bin/env python

import os
import sys

def identity(value):
    return value


def to_int(value: str):
    if value == '':
        return ''
    return f"{int(float(value))}"


def format_memory(value: str):
    if value == '':
        return ''
    try:
        memory = float(value) / GB
    except ValueError as e:
        print(f"Unable to convert {value}")
        raise e
    
    if memory < 0.1:
        memory = 0.1
    return f"{memory:4.1f}"

def format_runtime(value: str):
    if value == '':
        return ''
    runtime = float(value) / 10**9
    if runtime < 1:
        runtime = 1
    return f"{(int(runtime)):5d}"

# Columns to include and how the values should be formatted.
columns = {
    'E': identity, 
    'D': identity, 
    'C': identity,
    'J': to_int,
    'L': format_memory, 
    'P': format_runtime
}

GB = 1024 * 1024 * 1024

def column(index: str):
    return ord(index.lower()) - ord('a')


from pprint import pprint
def print_header(line: list):
    values = [ line[column(c)] for c in columns.keys() ]
    print(f"| {'|'.join(values)} |")
    print("|---|---|---|---|---:|---:|")


def print_row(line: list):
    values = list()
    for c,f in columns.items():
        values.append(f(line[column(c)]))
    print(f"| {'|'.join(values)} |")
    

def run(filename: str):
    with open(filename) as f:
        lines = f.read().splitlines(keepends=False)

    print_header(lines[0].split(','))
    for line in lines[1:]:
        print_row(line.split(','))    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("USAGE: csv2md.py /path/to/file.csv")
    else:
        run(sys.argv[1])

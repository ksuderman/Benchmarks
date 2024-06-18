#!/usr/bin/env python3
import os
import sys
from argparse import ArgumentParser
from typing import List


def do_filter(collection, f):
    '''
    Similar to the built-in filter function but we return an actual list object
    not just an iterable.

    :param collection: the collection to be filtered
    :param f: a function-like object used to filter the collection
    :return: a list object containing the elements x for which the funtion f(x)
            returned True.
    '''
    return [x for x in collection if f(x)]



def load_lines(filepath: str) -> List:
    '''
    Loads the contents of a file into a list of strings
    :param filepath: the path to the file to be loaded
    :return: a list of strings
    '''
    if not os.path.exists(filepath):
        raise FileNotFoundError(filepath)
    with open(filepath) as f:
        lines = f.read().splitlines(keepends=False)
    return lines


def parse_markdown(filepath: str, filter) -> list:
    '''
    Loads a GFM file into a list of strings using the filter function to remove
    unwanted elements

    :param filepath: the path to the file to be loaded.
    :param filter: a function-like object used to remove unwanted lines
    :return: a list of strings
    '''

    result = list()
    lines = load_lines(filepath)
    header = lines[0].split("|")[1:-1]
    result.append(header)
    for line in lines[2:]:
        if filter(line):
            row = line.split("|")[1:-1]
            result.append(row)
    return result


def parse_csv(filepath: str, filter) -> list:
    result = list()
    lines = load_lines(filepath)
    header = lines[0].split(",")
    result.append(header)
    for line in lines[1:]:
        if filter(line):
            result.append(line.split(","))
    return result


def calculate_averages(rows, columns):
    n = len(columns)
    results = [0.0] * n
    for row in rows:
        # print(row)
        for i in range(0, n):
            column = int(columns[i])
            # print(f"i={i} column={column}")
            try:
                results[i] += float(row[column])
            except:
                # Ignore malformed content.  The tool failed.
                pass
    for i in range(0, n):
        if len(rows) == 0:
            results[i] = 0.0
        else:
            results[i] = results[i] / len(rows)
    return results


def run(args):
    if args.file[0].endswith(".csv"):
        parse_data = parse_csv
    elif args.file[0].endswith(".md"):
        parse_data = parse_markdown
    else:
        print(f"ERROR: Unknown file type for {args.file[0]}")
        return

    columns = args.columns.split(",")
    # parse_data = parse_csv if args.csv else parse_markdown
    accept = lambda c: c in columns
    header = None
    rows = list()
    line = []
    if args.filter:
        line.extend(args.filter)
        def line_filter(line:str) -> bool:
            for f in args.filter:
                if f[0] not in line:
                    return False
            return True
    else:
        def line_filter(line: str) -> bool:
            return True

    for file in args.file:
        data = parse_data(file, line_filter)
        if header is None:
            header = data[0]
        rows.extend(data[1:])
    averages = calculate_averages(rows, columns)
    # for i in range(0, len(columns)):
    #     column = int(columns[i])
    #     print(f"{header[column]:<20}: {averages[i]:5.2f}")
    print_results_as_csv(args.filter, averages)


def print_results_as_csv(filters, averages):
    if filters:
        print(filters[0][0], end="")
        for f in filters[1:]:
            print(f", {f[0]}", end="")
    for i in range(0, len(averages)):
        print(f", {averages[i]:5.2f}", end="")
    print()


def print_args(args):
    print(f"Columns {args.columns}")
    if args.filter:
        print(f"\nFilterers")
        for filter in args.filter:
            print(filter)
    print("\nFiles")
    for file in args.file:
        print(file)


if __name__ == "__main__":
    epilog = """
When parsing markdown files the file can only contain a table with a header row.
General markdowm files, with content other than a table, are not supported.    
"""
    description = (
        "Calculate the averages for one or more columns in a CSV or Markdown file."
    )
    parser = ArgumentParser(prog="colavg", description=description, epilog=epilog)
    parser.add_argument(
        "-c",
        "--columns",
        action="store",
        help="averages will be calculated for these columns",
        required=True,
    )
    parser.add_argument("-f", "--filter", action="append", help="string used to filter rows", nargs='+')
    parser.add_argument("file", nargs="+", help="one or more files to be processed")

    args = parser.parse_args(sys.argv[1:])
    run(args)

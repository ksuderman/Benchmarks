import os
import sys
from functools import reduce

directory = '/Users/suderman/Workspaces/JHU/Ex2/rnaseq/results'


def accept(filepath: str) -> bool:
    return filepath.startswith('RNASeq_') and \
           filepath.endswith("Default.md") and \
           '8x64' not in filepath


def get_table(table, key):
    if key not in table:
        table[key] = dict()
    return table[key]


def add_to_list(table, key, value):
    if key not in table:
        table[key] = list()
    table[key].append(float(value))
    # print(f"added {value} for {key} length {len(table[key])}")


def calculate_average(values: list):
    total = reduce(lambda a,b: a+b, values)
    return total / len(values)


def print_results(table: dict) -> None:
    print("Tool,Dataset,Memory,Runtime")
    for size,sizes in table.items():
        # print(f"Printing results for size {size}")
        # sorted(sizes, 'runtime')
        for tool, tools in sizes.items():
            # print(f"Print results for tool {tool}")
            memory = calculate_average(tools['memory'])
            runtime = calculate_average(tools['runtime'])
            print(f"{tool.strip()},{size},{memory:5.1f},{runtime:5.1f}")


def process_file(filepath: str) -> None:
    pass

def run():
    table = dict()
    for file in os.listdir(directory):
        if accept(file):
            parts = file.split('_')
            size = parts[3]
            by_size = get_table(table, size)
            with open(os.path.join(directory,file)) as f:
                lines = f.read().splitlines(keepends=False)
            # print(f"There are {len(lines)} lines")
            for line in lines[2:]:
                parts = line.split('|')
                if 'ok' not in parts[3]:
                    # print(f"Skipping {line}")
                    continue
                tool = parts[1]
                memory = parts[4]
                runtime = parts[5]
                # print(size, tool, memory, runtime)
                # count += 1
                by_tool = get_table(by_size, tool)
                add_to_list(by_tool, 'memory', memory)
                add_to_list(by_tool, 'runtime', runtime)
    # from pprint import pprint
    # pprint(table)
    print_results(table)


if __name__ == '__main__':
    run()
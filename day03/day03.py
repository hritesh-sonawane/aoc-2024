#!/usr/bin/env python3

import re
import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
lines = ''.join(lines)

# Part 1
def calculate_mul_sum(lines):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, lines)

    return sum(int(x) * int(y) for x, y in matches)


# Part 2
def calculate_mul_sum_2(lines):
    mul_pattern = r'mul\((\d+),(\d+)\)'
    ctrl_pattern = r"(do\(\)|don't\(\))"

    active = True
    total = 0

    combined_pattern = f"{mul_pattern}|{ctrl_pattern}"
    matches = re.findall(combined_pattern, lines)

    for match in matches:
        if match[0] and match[1]:
            if active:
                total += int(match[0]) * int(match[1])
        elif match[2] == "do()":
            active = True
        elif match[2] == "don't()":
            active = False

    return total


part1 = calculate_mul_sum(lines)
print(f'Part 1: {part1}')

part2 = calculate_mul_sum_2(lines)
print(f'Part 2: {part2}')
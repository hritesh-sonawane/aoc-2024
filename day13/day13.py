#!/usr/bin/env python3

import sys
import re


with open(sys.argv[1], 'r') as f:
    puzzles = f.read().split("\n\n")

# https://www.purplemath.com/modules/cramers.htm
def solve_puzzle(puzzle, offset=0):
    a1, a2 = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", puzzle)[0]))
    c1 += offset
    c2 += offset
    
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))
    
    if (int(x) == x) and (int(y) == y):
        return tuple(map(int, (x, y)))
    
    return (0, 0)


part1 = 0
part2 = 0
for puzzle in puzzles:
    a, b = solve_puzzle(puzzle)
    part1 += (a * 3) + b
    
    ar, br = solve_puzzle(puzzle, offset=10000000000000)
    part2 += (ar * 3) + br
    
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().split("\n\n")
    
patterns = lines[0].split(", ")
designs = lines[1].split("\n")

# part 1
def can_form_design(patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[len(design)]

part1 = 0
for design in designs:
    if can_form_design(patterns, design):
        part1 += 1

print(f'Part 1: {part1}')


# part 2
def count_designs(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[len(design)]

part2 = 0
for design in designs:
    if can_form_design(patterns, design):
        part2 += count_designs(patterns, design)

print(f'Part 2: {part2}')
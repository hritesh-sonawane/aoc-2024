#!/usr/bin/env python3

import math
import re
import sys
import matplotlib.pyplot as plt


with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f]
    
width, height = (101, 103) if sys.argv[1] == "input.txt" else (11, 7)

def safety_score(robots):
    quadrants = [0] * 4
    midw, midh = width // 2, height // 2

    for x, y in robots:
        if x < midw and y < midh:
            quadrants[0] += 1
        elif x < midw and y > midh:
            quadrants[1] += 1
        elif x > midw and y < midh:
            quadrants[2] += 1
        elif x > midw and y > midh:
            quadrants[3] += 1

    return math.prod(quadrants)

robots = [
    tuple(map(int, re.findall(r'-?\d+', line)))
    for line in lines
]

part1_robots = [
    ((x + dx * 100) % width, (y + dy * 100) % height)
    for x, y, dx, dy in robots
]
part1 = safety_score(part1_robots)
print(f'Part 1: {part1}')


time = []
safe_scores = []

for i in range(10000):
    snap = [
        ((x + dx * i) % width, (y + dy * i) % height)
        for x, y, dx, dy in robots
    ]
    time.append(i)
    safe_scores.append(safety_score(snap))


plt.plot(time, safe_scores)
plt.show()
# look for the peak in the plotted graph

part2 = ""
print(f'Part 2: {part2}')
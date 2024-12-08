#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())
antennas = {}

for r in range(rows):
    for c in range(cols):
        char = lines[r][c]
        if char != '.':
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((r, c))


def calc_antinodes_part1(antenna_list):
    antinode_set = set()
    
    for i in range(len(antenna_list)):
        for j in range(i + 1, len(antenna_list)):
            r1, c1 = antenna_list[i]
            r2, c2 = antenna_list[j]

            dr, dc = r2 - r1, c2 - c1

            for (r, c), direction in [(antenna_list[i], -1), (antenna_list[j], 1)]:
                antinode = (r + direction * dr, c + direction * dc)
                if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                    antinode_set.add(antinode)

    return antinode_set


def calc_antinodes_part2(antenna_list):
    antinode_set = set()
    
    for i in range(len(antenna_list)):
        for j in range(i + 1, len(antenna_list)):
            r1, c1 = antenna_list[i]
            r2, c2 = antenna_list[j]

            dr, dc = r2 - r1, c2 - c1

            for (start_r, start_c), direction in [(antenna_list[i], -1), (antenna_list[j], 1)]:
                pos = (start_r, start_c)
                
                while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                    antinode_set.add(pos)
                    pos = (pos[0] + direction * dr, pos[1] + direction * dc)

    return antinode_set


unique_antinodes_part1 = set()
for freq, pos in antennas.items():
    unique_antinodes_part1.update(calc_antinodes_part1(pos))

unique_antinodes_part2 = set()
for freq, pos in antennas.items():
    unique_antinodes_part2.update(calc_antinodes_part2(pos))


part1 = len(unique_antinodes_part1)
print(f'Part 1: {part1}')

part2 = len(unique_antinodes_part2)
print(f'Part 2: {part2}')
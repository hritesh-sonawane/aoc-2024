#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

ROWS = len(lines)
COLS = len(lines[0])
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r in range(ROWS):
    for c in range(COLS):
        if lines[r][c] == '^':
            guard_row, guard_col = r, c

part1 = 0
part2 = 0

# obs -> place obstruction
for obs_row in range(ROWS):
    for obs_col in range(COLS):
        r, c = guard_row, guard_col
        direction_index = 0  # 0 = up, 1 = right, 2 = down, 3 = left
        visited_states = set()
        visited_positions = set()

        while True:
            if (r, c, direction_index) in visited_states:
                part2 += 1
                break

            # current state
            visited_states.add((r, c, direction_index))
            visited_positions.add((r, c))

            # next pos
            dr, dc = DIRECTIONS[direction_index]
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                if lines[obs_row][obs_col] == '#':
                    part1 = max(part1, len(visited_positions))
                break

            if lines[nr][nc] == '#' or (nr == obs_row and nc == obs_col):
                direction_index = (direction_index + 1) % 4  # turn right (clockwise)
            else:
                r = nr
                c = nc

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
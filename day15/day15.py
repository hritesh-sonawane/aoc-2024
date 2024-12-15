#!/usr/bin/env python3

import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
    lines = f.read().split('\n\n')

grid = defaultdict(lambda: "#")
for i, line in enumerate(lines[0].splitlines()):
    for j, c in enumerate(line):
        grid[(i, j)] = c

robot_x, robot_y = None, None
for pos, value in grid.items():
    if value == '@':
        robot_x, robot_y = pos
        break

for dir in lines[1].replace('\n', ''):
    assert grid[robot_x, robot_y] == '@'
    
    dx, dy = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}[dir]
    next_x, next_y = robot_x + dx, robot_y + dy
    
    while grid[next_x, next_y] == 'O':
        next_x, next_y = next_x + dx, next_y + dy
    if grid[next_x, next_y] == '.':
        while (next_x, next_y) != (robot_x, robot_y):
            grid[next_x, next_y] = grid[next_x - dx, next_y - dy]
            next_x, next_y = next_x - dx, next_y - dy
        grid[robot_x, robot_y] = '.'
        robot_x, robot_y = robot_x + dx, robot_y + dy

part1 = 0
for pos, value in grid.items():
    if value == 'O':
        part1 += pos[0] * 100 + pos[1]

#####

lines[0] = lines[0].replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
grid = defaultdict(lambda: "#")
for i, line in enumerate(lines[0].splitlines()):
    for j, c in enumerate(line):
        grid[(i, j)] = c

robot_x, robot_y = None, None
for pos, value in grid.items():
    if value == '@':
        robot_x, robot_y = pos
        break

def can_move(x, y, dx, dy):
    target_x = x + dx
    target_y = y + dy
    target = (target_x, target_y)
    if grid[target] == '.':
        return True
    if grid[target] == '#':
        return False
    if dx == 0:
        return can_move(target_x, target_y, dx, dy)
    else:
        lr = -1 if grid[target] == ']' else 1
        return can_move(target_x, target_y, dx, dy) and can_move(target_x, target_y + lr, dx, dy)

def move(x, y, dx, dy):
    target_x = x + dx
    target_y = y + dy
    target = (target_x, target_y)
    if grid[target] != '.':
        if dx == 0:
            move(target_x, target_y, dx, dy)
        else:
            if grid[target] in '[]':
                lr = -1 if grid[target] == ']' else 1
                move(x + dx, y + dy + lr, dx, dy)
                move(x + dx, y + dy, dx, dy)
    grid[target] = grid[(x, y)]
    grid[(x, y)] = '.'

for dir in lines[1].replace('\n', ''):
    assert grid[robot_x, robot_y] == '@'
    
    dx, dy = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}[dir]
    next_x, next_y = robot_x + dx, robot_y + dy
    if can_move(robot_x, robot_y, dx, dy):
        move(robot_x, robot_y, dx, dy)
        robot_x, robot_y = next_x, next_y

part2 = 0
for pos, value in grid.items():
    if value == '[':
        part2 += pos[0] * 100 + pos[1]

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
#!/usr/bin/env python3

import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

def parse_input(lines):
    walls = set()
    start, end = None, None
    for j, row in enumerate(lines):
        for i, c in enumerate(row.strip()):
            if c == "#":
                walls.add(i + j * 1j)   # complex numbers lol
            elif c == "S":
                start = i + j * 1j
            elif c == "E":
                end = i + j * 1j
    return walls, start, end

def get_turn_cost(old_dir, new_dir, directions):
    right_turns = (directions.index(new_dir) - directions.index(old_dir)) % 4
    left_turns = (4 - right_turns) % 4
    return min(left_turns, right_turns) * 1000

def part1(walls, start, end):
    directions = [1, -1j, -1, 1j]
    q = {(start, 1, 0)}   # (pos, direction, points)
    points = defaultdict(dict)   # {pos: {direction: points}}
    points[start][1] = 0

    while q:
        pos, old_dir, old_points = q.pop()
        for new_dir in directions:
            new_pos = pos + new_dir
            if new_pos in walls:
                continue

            # update cost to look in new direction
            points[pos][new_dir] = min(points[pos].get(new_dir, float("inf")),
                                       old_points + get_turn_cost(old_dir, new_dir, directions))
            # cost to move in new direction
            new_points = points[pos][new_dir] + 1

            # add to q if new position is not visited or has a lower cost
            if new_pos not in points or points[new_pos].get(new_dir, float("inf")) > new_points:
                points[new_pos][new_dir] = new_points
                q.add((new_pos, new_dir, new_points))

    if end not in points or not points[end]:
        print("No valid path to end found in part1.")
        return float("inf"), points

    return min(points[end].values()), points

def part2(walls, start, end, min_cost, points):
    directions = [1, -1j, -1, 1j]
    if end not in points or not points[end]:
        print("No valid path to end found in part2.")
        return 0

    part2_set = {end}   # set of all positions part of an optimal path
    q = {(end, min(points[end], key=points[end].get), min_cost)}   # (pos, direction, points)

    while q:
        pos, cur_dir, cur_points = q.pop()
        for prev_dir in directions:
            prev_pos = pos - prev_dir   # walk backward
            # if the current pos and cost can be achieved from prev_pos, add prev_pos to optimal path
            if prev_pos in points and points[prev_pos][prev_dir] == cur_points - 1 - get_turn_cost(prev_dir, cur_dir, directions):
                part2_set.add(prev_pos)
                q.add((prev_pos, prev_dir, points[prev_pos][prev_dir]))

    return len(part2_set)



walls, start, end = parse_input(lines)
min_cost, points = part1(walls, start, end)
print(f"Part 1: {min_cost}")
print(f"Part 2: {part2(walls, start, end, min_cost, points)}")
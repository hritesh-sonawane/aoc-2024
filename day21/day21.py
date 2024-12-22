#!/usr/bin/env python3

import sys
from collections import deque
from itertools import product
from functools import cache


with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

def find_best_x_to_y(keypad, x, y):
    if x == y:
        return ["A"]

    q = deque([(x[0], x[1], "")])
    best_length = float("inf")
    optimal_paths = []

    while q:
        r, c, path = q.popleft()

        for nr, nc, move in [(r + 1, c, "v"), (r - 1, c, "^"), (r, c + 1, ">"), (r, c - 1, "<")]:
            if (nr, nc) not in keypad:
                continue

            new_path = path + move

            if (nr, nc) == y:
                optimal_paths.append(new_path + "A")
                best_length = min(best_length, len(new_path) + 1)
            elif len(new_path) < best_length:
                q.append((nr, nc, new_path))

    return optimal_paths

def keys_to_paths(keypad_paths, line):
    path_segments = [keypad_paths[(b1, b2)] for b1, b2 in zip("A" + line, line)]
    return ["".join(segment) for segment in product(*path_segments)]

@cache
def get_length(line, depth):
    if depth == 0:
        return len(line)

    return sum(
        min(get_length(seq, depth - 1) for seq in dir_pad_paths[(p1, p2)])
        for p1, p2 in zip("A" + line, line)
    )

def init_keypads():
    num_pad = {
        (0, 0): "7", (0, 1): "8", (0, 2): "9",
        (1, 0): "4", (1, 1): "5", (1, 2): "6",
        (2, 0): "1", (2, 1): "2", (2, 2): "3",
        (3, 1): "0", (3, 2): "A",
    }

    dir_pad = {
        (0, 1): "^", (0, 2): "A",
        (1, 0): "<", (1, 1): "v", (1, 2): ">",
    }

    num_pad_paths = {
        (num_pad[p1], num_pad[p2]): find_best_x_to_y(num_pad, p1, p2)
        for p1 in num_pad for p2 in num_pad
    }

    dir_pad_paths = {
        (dir_pad[p1], dir_pad[p2]): find_best_x_to_y(dir_pad, p1, p2)
        for p1 in dir_pad for p2 in dir_pad
    }

    return num_pad_paths, dir_pad_paths

def calc_scores(lines, num_pad_paths):
    part1, part2 = 0, 0

    for line in lines:
        best_length = float("inf")
        best_length2 = float("inf")

        for path1 in keys_to_paths(num_pad_paths, line):
            best_length = min(best_length, get_length(path1, 2))
            best_length2 = min(best_length2, get_length(path1, 25))

        part1 += int(line[:-1]) * best_length
        part2 += int(line[:-1]) * best_length2

    return part1, part2


num_pad_paths, dir_pad_paths = init_keypads()
part1, part2 = calc_scores(lines, num_pad_paths)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
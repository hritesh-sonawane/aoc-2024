#!/usr/bin/env python3

from collections import deque
import sys


with open(sys.argv[1], 'r') as f:
    blocks = [tuple(map(int, line.split(",")))[::-1] for line in map(str.strip, f.readlines())]

if sys.argv[1] == "input.txt":
    ROWS, COLS, part1_num = 71, 71, 1024
else:
    ROWS, COLS, part1_num = 7, 7, 12

def bfs_shortest_path(rows, cols, blocks, max_blocks):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    q = deque([(0, 0, 0)])   # (row, col, dist)

    while q:
        r, c, dist = q.popleft()

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if r == rows - 1 and c == cols - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in blocks[:max_blocks] and
                (nr, nc) not in visited):
                q.append((nr, nc, dist + 1))

    return -1

def find_blocking_byte(rows, cols, blocks):
    # binary search
    left, right = 0, len(blocks)
    res = (-1, -1)

    while left < right:
        mid = (left + right) // 2

        if bfs_shortest_path(rows, cols, blocks, mid) != -1:
            left = mid + 1
        else:
            res = blocks[mid - 1]   # last block that allowed a path
            right = mid

    return res


part1 = bfs_shortest_path(ROWS, COLS, blocks, part1_num)
print(f'Part 1: {part1}')

part2 = find_blocking_byte(ROWS, COLS, blocks)
print(f'Part 2: {part2[1]},{part2[0]}')
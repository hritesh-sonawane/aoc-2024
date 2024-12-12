#!/usr/bin/env python3

import sys
from collections import deque


with open(sys.argv[1], 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])
regions = []
seen = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region = {(r, c)}
        q = deque([(r, c)])
        crop = grid[r][c]
        
        while q:
            cr, cc = q.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if grid[nr][nc] != crop:
                    continue
                if (nr, nc) in region:
                    continue
                region.add((nr, nc))
                q.append((nr, nc))
        seen |= region
        regions.append(region)

def perimeter(region):
    res = 0
    for (r, c) in region:
        res += 4
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in region:
                res -= 1
    return res

part1 = sum(len(region) * perimeter(region) for region in regions)
print(f'Part 1: {part1}')


def sides(region):
    corner_candidates = set()
    for r, c in region:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
    
    corners = 0
    for cr, cc in corner_candidates:
        config = [(sr, sc) in region for sr, sc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners

part2 = sum(len(region) * sides(region) for region in regions)
print(f'Part 2: {part2}')
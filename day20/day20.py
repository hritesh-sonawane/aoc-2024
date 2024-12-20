#!/usr/bin/env python3

from collections import defaultdict, deque
import sys


with open(sys.argv[1], 'r') as f:
    grid = list(map(str.strip, f.readlines()))

target_savings = 100 if sys.argv[1] == "input.txt" else 1

def find_distances(grid, start_pos):
    rows, cols = len(grid), len(grid[0])
    distances = {}
    q = deque([(start_pos[0], start_pos[1], 0)])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    while q:
        r, c, dist = q.popleft()
        if (r, c) in distances:
            continue
        distances[(r, c)] = dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                q.appendleft((nr, nc, dist + 1))
                
    return distances


def calculate_shortcuts(grid, distances, target_savings, max_cheat_len=None):
    rows, cols = len(grid), len(grid[0])
    shortcuts = defaultdict(int)
    
    if max_cheat_len is None:
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    if (r, c) not in distances or (r2, c2) not in distances:
                        continue
                    time_saved = distances[(r2, c2)] - distances[(r, c)] - 2
                    if time_saved >= target_savings:
                        shortcuts[time_saved] += 1
    else:
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in distances:
                    continue
                for cheat_len in range(2, max_cheat_len + 1):
                    for dr in range(cheat_len + 1):
                        dc = cheat_len - dr
                        for r2, c2 in set([(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)]):
                            if (r2, c2) not in distances:
                                continue
                            time_saved = distances[(r2, c2)] - distances[(r, c)] - cheat_len
                            if time_saved >= target_savings:
                                shortcuts[time_saved] += 1
    
    return sum(shortcuts.values())


start_pos = None
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            start_pos = (r, c)
            break
    if start_pos:
        break
    
distances = find_distances(grid, start_pos)

part1 = calculate_shortcuts(grid, distances, target_savings)
print(f'Part 1: {part1}')

part2_target = 50 if target_savings == 1 else target_savings
part2 = calculate_shortcuts(grid, distances, part2_target, max_cheat_len=20)
print(f'Part 2: {part2}')
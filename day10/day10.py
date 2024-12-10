#!/usr/bin/env python3

import sys
from collections import deque
from functools import lru_cache


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


def calc_scores(lines):
    grid = [[int(ch) for ch in line.strip()] for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    total_score = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # bfs to calculate the score
                q = deque([(r, c, 0)])   # (row, col, curr_height)
                visited = set()
                visited.add((r, c))
                reachable_nines = 0

                while q:
                    x, y, height = q.popleft()
                    if grid[x][y] == 9:
                        reachable_nines += 1
                        continue

                    for dr, dc in directions:
                        nr, nc = x + dr, y + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                            if grid[nr][nc] == height + 1:
                                visited.add((nr, nc))
                                q.append((nr, nc, height + 1))

                total_score += reachable_nines

    return total_score


def count_trails(grid, r, c):
    rows = len(grid) 
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    @lru_cache(maxsize=None)
    def dfs(x, y, height, visited):
        visited = tuple(sorted(visited))   # for caching
        
        if grid[x][y] == 9:
            return 1
        
        trail_count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                    0 <= nx < rows and 0 <= ny < cols 
                    and grid[nx][ny] == height + 1
                    and (nx, ny) not in visited
               ):
                    new_visited = list(visited)
                    new_visited.append((nx, ny))
                    trail_count += dfs(nx, ny, height + 1, tuple(sorted(new_visited)))
        
        return trail_count
    return dfs(r, c, 0, ((r, c),))


def calc_ratings(lines):
    grid = [list(map(int, line.strip())) for line in lines]
    rows, cols = len(grid), len(grid[0])
    total_rating = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                rating = count_trails(grid, r, c)
                total_rating += rating

    return total_rating


part1 = calc_scores(lines)
print(f'Part 1: {part1}')

part2 = calc_ratings(lines)
print(f'Part 2: {part2}')
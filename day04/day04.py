#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    grid = [line.strip() for line in f.readlines()]
    
ROWS = len(grid)
COLS = len(grid[0])

# Part 1
def count_xmas(grid, word):
    word_len = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    count = 0

    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in directions:
                if all(
                    (r + dr * k) in range(ROWS) and
                    (c + dc * k) in range(COLS) and
                    grid[r + dr * k][c + dc * k] == word[k]
                    for k in range(word_len)
                ):
                    count += 1
    return count


# Part 2
def count_x_mas(grid):
    def top_left(r, c):
        return r - 1, c - 1
    def top_right(r, c):
        return r - 1, c + 1
    def bottom_left(r, c):
        return r + 1, c - 1
    def bottom_right(r, c):
        return r + 1, c + 1
    
    char_map = {"A": [], "M": [], "S": []}
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] in char_map:
                char_map[grid[r][c]].append((r, c))
    
    count = 0
    
    for r, c in char_map["A"]:
        if top_left(r, c) in char_map["M"]:
            if bottom_left(r, c) in char_map["M"] and top_right(r, c) in char_map["S"] and bottom_right(r, c) in char_map["S"]:
                count += 1
            elif top_right(r, c) in char_map["M"] and bottom_left(r, c) in char_map["S"] and bottom_right(r, c) in char_map["S"]:
                count += 1
        elif bottom_right(r, c) in char_map["M"]:
            if bottom_left(r, c) in char_map["M"] and top_right(r, c) in char_map["S"] and top_left(r, c) in char_map["S"]:
                count += 1
            elif top_right(r, c) in char_map["M"] and bottom_left(r, c) in char_map["S"] and top_left(r, c) in char_map["S"]:
                count += 1
    
    return count



part1 = count_xmas(grid, "XMAS")
print(f'Part 1: {part1}')

part2 = count_x_mas(grid)
print(f'Part 2: {part2}')
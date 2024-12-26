#!/usr/bin/env python3

import sys


with open(sys.argv[1], "r") as file:
    grids = file.read().strip().split("\n\n")

grid_categories = {"locked": [], "unlocked": []}

for grid in grids:
    rows = [row for row in grid.split("\n") if row]
    if not rows or len(rows[0]) == 0:
        continue

    col_counts = [sum(1 for row in rows if row[col] == "#") for col in range(len(rows[0]))]
    category_key = "locked" if rows[0][0] == "#" else "unlocked"
    grid_categories[category_key].append(col_counts)

count = 0
for locked in grid_categories["locked"]:
    for unlocked in grid_categories["unlocked"]:
        if all(locked + unlocked <= 7 for locked, unlocked in zip(locked, unlocked)):
            count += 1

print(f"Part 1: {count}")
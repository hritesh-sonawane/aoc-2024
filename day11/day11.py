#!/usr/bin/env python3

import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


# def count_stones(lines, blinks):
#     stones = deque(map(int, lines[0].strip().split()))
    
#     for _ in range(blinks):
#         next_stones = deque()
        
#         while stones:
#             stone = stones.popleft()
#             if stone == 0:
#                 next_stones.append(1)
#             elif len(str(stone)) % 2 == 0:
#                 mid = len(str(stone)) // 2
#                 next_stones.append(int(str(stone)[:mid]))
#                 next_stones.append(int(str(stone)[mid:]))
#             else:
#                 next_stones.append(stone * 2024)
#         stones = next_stones
    
#     return len(stones)


def count_stones_optimized(lines, blinks):
    stones = list(map(int, lines[0].strip().split()))
    cache = defaultdict(int)

    def process_stone(stone, remaining_blinks):
        if remaining_blinks == 0:
            return 1   # base case
        
        key = (stone, remaining_blinks)
        if key in cache:
            return cache[key]
        
        if stone == 0:
            res = process_stone(1, remaining_blinks - 1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            res = process_stone(left, remaining_blinks - 1) + process_stone(right, remaining_blinks - 1)
        else:
            res = process_stone(stone * 2024, remaining_blinks - 1)
        
        cache[key] = res
        return res

    total_stones = sum(process_stone(stone, blinks) for stone in stones)
    return total_stones


part1 = count_stones_optimized(lines, 25)
print(f'Part 1: {part1}')

part2 = count_stones_optimized(lines, 75)
print(f'Part 2: {part2}')
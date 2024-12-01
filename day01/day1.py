#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)

# Part 1
def total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance


# Part 2
def similarity_score(left_list, right_list):
    right_count = {}
    
    for num in right_list:
        if num in right_count:
            right_count[num] += 1
        else:
            right_count[num] = 1

    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count.get(num, 0)

    return similarity_score


part1 = total_distance(left_list, right_list)
print(f'Part 1: {part1}')

part2 = similarity_score(left_list, right_list)
print(f'Part 2: {part2}')
#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

def can_produce_value(test_val, nums):
    def dfs(index, curr_val):
        if index == len(nums):
            return curr_val == test_val
        if dfs(index + 1, curr_val + nums[index]):
            return True
        if dfs(index + 1, curr_val * nums[index]):
            return True
        return False

    return dfs(1, nums[0])

def can_produce_value_with_concat(test_val, nums):
    def dfs(index, curr_val):
        if index == len(nums):
            return curr_val == test_val
        if dfs(index + 1, curr_val + nums[index]):
            return True
        if dfs(index + 1, curr_val * nums[index]):
            return True
        concat_value = int(str(curr_val) + str(nums[index]))
        if dfs(index + 1, concat_value):
            return True
        return False

    return dfs(1, nums[0])


part1 = 0
part2 = 0
for line in lines:
    test_val, nums = line.split(': ')
    test_val = int(test_val)
    nums = list(map(int, nums.split()))
    if can_produce_value(test_val, nums):
        part1 += test_val
        part2 += test_val
    elif can_produce_value_with_concat(test_val, nums):
        part2 += test_val


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
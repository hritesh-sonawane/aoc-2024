#!/usr/bin/env python3

import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
    nums = list(map(int, f.readlines()))
    
def next_num(x):
    x ^= (x * 64) % 16777216
    x ^= (x // 32) % 16777216
    x ^= (x * 2048) % 16777216
    return x

part1 = 0
seq_totals = defaultdict(int)
for num in nums:
    seen = set()
    res = []
    for _ in range(2000):
        num = next_num(num)
        res.append(num % 10)
    part1 += num
    
    diffs = [y - x for x, y in zip(res, res[1:])]
    for n, seq1, seq2, seq3, seq4 in zip(res[4:], diffs, diffs[1:], diffs[2:], diffs[3:]):
        seq = (seq1, seq2, seq3, seq4)
        if seq in seen: 
            continue
        seen.add(seq)
        seq_totals[seq] += n


print(f'Part 1: {part1}')

part2 = seq_totals[max(seq_totals, key=seq_totals.get)]
print(f'Part 2: {part2}')
#!/usr/bin/env python3

import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
    pairs = [line.strip().split('-') for line in f.readlines()]

conns = defaultdict(set)
for a, b in pairs:
    conns[a].add(b)
    conns[b].add(a)

triples = set()
for conn in conns:
    for nei in conns[conn]:
        for nn in conns[nei]:
            if conn in conns[nn]:
                triples.add(tuple(sorted([conn, nei, nn])))

part1 = len([t for t in triples if any(x.startswith("t") for x in t)])
print(f'Part 1: {part1}')


passwords = set()

def build_set(conn, group):
    password = ','.join(sorted(group))
    if password in passwords: 
        return
    passwords.add(password)
    
    for nei in conns[conn]:
        if nei in group: 
            continue
        if any(nei not in conns[node] for node in group): 
            continue
        build_set(nei, {*group, nei})

groups = set()
for conn in conns:
    build_set(conn, {conn})

part2 = max(passwords, key=len)
print(f'Part 2: {part2}')
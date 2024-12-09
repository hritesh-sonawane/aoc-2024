#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    data = list(map(int, f.read().strip()))

def calc_checksum(data):
    disk = []
    for i in range(0, len(data), 2):
        disk.extend(data[i] * [i // 2])
        if i + 1 < len(data):
            disk.extend(data[i + 1] * [-1])
    
    empties = [i for i, val in enumerate(disk) if val == -1]
    i = 0

    while True:
        while disk[-1] == -1:
            disk.pop()
        target = empties[i]
        
        if target >= len(disk):
            break
        
        disk[target] = disk.pop()
        i += 1    

    return sum(i * val for i, val in enumerate(disk) if val != -1)


def compact_and_checksum(data):
    is_file = True
    files = {}
    spaces = []
    ptr = 0

    for i, size in enumerate(data):
        if is_file:
            files[i // 2] = (ptr, size)
        else:
            spaces.append((ptr, size))
        is_file = not is_file
        ptr += size
    
    for fid in reversed(files):
        loc, file_size = files[fid]
        space_id = 0
        
        while space_id < len(spaces):
            space_loc, space_size = spaces[space_id]
            if space_loc > loc:
                break
            if space_size == file_size:
                files[fid] = (space_loc, file_size)
                spaces.pop(space_id)
                break
            if space_size > file_size:
                files[fid] = (space_loc, file_size)
                spaces[space_id] = (space_loc + file_size, space_size - file_size)
                break
            space_id += 1

    checksum = 0
    for fid, (loc, size) in files.items():
        for i in range(loc, loc + size):
            checksum += fid * i

    return checksum


part1 = calc_checksum(data)
print(f'Part 1: {part1}')

part2 = compact_and_checksum(data)
print(f'Part 2: {part2}')
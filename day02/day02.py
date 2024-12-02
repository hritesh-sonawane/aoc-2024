#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
# Part 1
def is_report_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return increasing or decreasing

def count_safe_reports(lines):
    count = 0
    
    for line in lines:
        report = list(map(int, line.split()))
        if is_report_safe(report):
            count += 1
    
    return count


# Part 2
def is_report_safe_w_dampener(report):
    # differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # if is_report_safe(report):
    #     return True
    
    # for i in range(len(report)):
    #     if i == 0:
    #         modified_diff = differences[1:]
    #     elif i == len(report) - 1:
    #         modified_diff = differences[:-1]
    #     else:
    #         # remove a middle level; merge the adj diffs
    #         modified_diff = (
    #             differences[:i - 1] +
    #             [report[i + 1] - report[i - 1]] +
    #             differences[i + 1:]
    #         )
        
    #     if is_report_safe(modified_diff):
    #         return True
        
    # return False
    
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        
        if is_report_safe(modified_report):
            return True
    
    return False

def count_safe_reports_w_dampener(lines):
    count = 0
    
    for line in lines:
        report = list(map(int, line.split()))
        if is_report_safe_w_dampener(report):
            count += 1
    
    return count

    
part1 = count_safe_reports(lines)
print(f'Part 1: {part1}')

part2 = count_safe_reports_w_dampener(lines)
print(f'Part 2: {part2}')
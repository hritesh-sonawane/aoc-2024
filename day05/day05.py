#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
    
def parse_input(lines):
    rules = []
    updates = []
    reading_rules = True

    for line in lines:
        if not line.strip():
            reading_rules = False
            continue
        if reading_rules:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates


def build_graph(rules):
    graph = {}
    for x, y in rules:
        if x not in graph:
            graph[x] = []
        graph[x].append(y)
    return graph


def validate_update(update, graph):
    positions = {page: i for i, page in enumerate(update)}
    return all(positions[x] < positions[y] for x in graph for y in graph[x] if x in positions and y in positions)


def process_updates_1(lines):
    rules, updates = parse_input(lines)
    graph = build_graph(rules)
    
    middle_sum = 0
    for update in updates:
        if validate_update(update, graph):
            middle_sum += update[len(update) // 2]
    
    return middle_sum


def topological_sort(update, graph):
    in_degree = {page: 0 for page in update}
    sorted_order = []

    for page in update:
        for dependent_page in graph.get(page, []):
            if dependent_page in in_degree:
                in_degree[dependent_page] += 1

    zero_degree_pages = [page for page in update if in_degree[page] == 0]
    
    while zero_degree_pages:
        curr_page = zero_degree_pages.pop()
        sorted_order.append(curr_page)
        for nei in graph.get(curr_page, []):
            if nei in in_degree:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    zero_degree_pages.append(nei)

    return sorted_order


def process_updates_2(lines):
    rules, updates = parse_input(lines)
    graph = build_graph(rules)

    middle_sum = 0
    for update in updates:
        update = list(map(int, update))
        
        if all(update.index(x) < update.index(y) for x in update for y in graph.get(x, []) if y in update):
            continue
        
        sorted_update = topological_sort(update, graph)
        middle_sum += sorted_update[len(sorted_update) // 2]

    return middle_sum



part1 = process_updates_1(lines)
print(f'Part 1: {part1}')

part2 = process_updates_2(lines)
print(f'Part 2: {part2}')
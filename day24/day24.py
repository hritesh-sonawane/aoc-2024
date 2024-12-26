#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass


with open(sys.argv[1], "r") as file:
    content = file.read()

@dataclass
class Wire:
    inputs: list[str]
    operation: str
    output: str

operations = {
    "OR": lambda a, b: a | b,
    "AND": lambda a, b: a & b,
    "XOR": lambda a, b: a ^ b,
}

def evaluate_wire(wire_name):
    if wire_name in initial_values:
        return initial_values[wire_name]
    connection = connections[wire_name]
    return operations[connection.operation](
        evaluate_wire(connection.inputs[0]), evaluate_wire(connection.inputs[1])
    )

initial_matches = re.findall(r"(.{3}): ([01])", content)
initial_values = {name: int(value) for name, value in initial_matches}

connection_lines = content.split("\n\n")[1].splitlines()
connections = {}
for line in connection_lines:
    input1, operation, input2, _, output = line.strip().split()
    connections[output] = Wire([input1, input2], operation, output)

def solve():
    z_wires = sorted(
        [name for name in connections if name.startswith("z")], reverse=True
    )
    result_bits = [evaluate_wire(name) for name in z_wires]
    return int("".join(map(str, result_bits)), 2)

part1_result = solve()
print(f"Part 1: {part1_result}")

def evaluate_wire_with_init(wire_name, init_values):
    match = re.match(r'(x|y)(\d{2})', wire_name)
    if match:
        var, index = match.groups()
        return init_values[var][int(index)]
    connection = connections[wire_name]
    return operations[connection.operation](
        evaluate_wire_with_init(connection.inputs[0], init_values),
        evaluate_wire_with_init(connection.inputs[1], init_values),
    )

def create_wire_name(prefix, index):
    return f"{prefix}{str(index).zfill(2)}"

# help from gpt :)
def validate_bit(index):
    for x_val in range(2):
        for y_val in range(2):
            for carry in range(2):
                x_bits = [0] * (44 - index) + [x_val]
                y_bits = [0] * (44 - index) + [y_val]
                if index > 0:
                    x_bits += [carry] + [0] * (index - 1)
                    y_bits += [carry] + [0] * (index - 1)
                elif carry > 0:
                    continue
                x_bits.reverse()
                y_bits.reverse()
                result = evaluate_wire_with_init(
                    create_wire_name("z", index), {"x": x_bits, "y": y_bits}
                )
                if result != (x_val + y_val + carry) % 2:
                    return False
    return True

def find_connection(op=None, input1=None, input2=None):
    for conn in connections.values():
        if op and op != conn.operation:
            continue
        if input1 and input1 not in conn.inputs:
            continue
        if input2 and input2 not in conn.inputs:
            continue
        return conn

def swap_connections(wire1, wire2):
    connections[wire1], connections[wire2] = connections[wire2], connections[wire1]

def fix_bit(index):
    print(f"Issue with index = {index}")
    prev_and = find_connection(op="AND", input1=create_wire_name("x", index - 1), input2=create_wire_name("y", index - 1))
    prev_xor = find_connection(op="XOR", input1=create_wire_name("x", index - 1), input2=create_wire_name("y", index - 1))
    m2 = find_connection(op="AND", input1=prev_xor.output)
    m1 = find_connection(op="OR", input1=m2.output, input2=prev_and.output)
    n_xor = find_connection(op="XOR", input1=create_wire_name("x", index), input2=create_wire_name("y", index))
    z_wire = find_connection(op="XOR", input1=n_xor.output, input2=m1.output)

    if z_wire is None:
        z_wire = connections[create_wire_name("z", index)]
        swap_list = list(set(z_wire.inputs) ^ set([n_xor.output, m1.output]))
    if z_wire.output != create_wire_name("z", index):
        swap_list = [create_wire_name("z", index), z_wire.output]
    swap_connections(*swap_list)
    return swap_list

part2_results = []
for i in range(45):
    if validate_bit(i):
        continue
    part2_results.extend(fix_bit(i))

print(f"Part 2: {','.join(sorted(part2_results))}")
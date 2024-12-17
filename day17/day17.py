#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    data = f.read().splitlines()
    
def run_program(registers, program):
    def combo_operand(value, A, B, C):
        if value in [0, 1, 2, 3]:
            return value
        elif value == 4:
            return A
        elif value == 5:
            return B
        elif value == 6:
            return C

    A, B, C = registers
    pointer = 0
    outputs = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:   # adv
            A //= 2 ** combo_operand(operand, A, B, C)
        elif opcode == 1:   # bxl
            B ^= operand
        elif opcode == 2:   # bst
            B = combo_operand(operand, A, B, C) % 8
        elif opcode == 3:   # jnz
            if A != 0:
                pointer = operand
                continue   # skip pointer increment
        elif opcode == 4:   # bxc
            B ^= C
        elif opcode == 5:   # out
            outputs.append(combo_operand(operand, A, B, C) % 8)
        elif opcode == 6:   # bdv
            B = A // (2 ** combo_operand(operand, A, B, C))
        elif opcode == 7:   # cdv
            C = A // (2 ** combo_operand(operand, A, B, C))

        pointer += 2

    return outputs

def part1(data):
    registers = [
        int(data[0].split(": ")[1]),   # register A
        int(data[1].split(": ")[1]),   # register B
        int(data[2].split(": ")[1]),   # register C
    ]
    program = list(map(int, data[4].split(": ")[1].split(",")))

    res = run_program(registers, program)
    return ",".join(map(str, res))

def part2(data):
    program = list(map(int, data[4].split(": ")[1].split(",")))

    # start A at val based on observed tail patterns
    # https://youtu.be/02CLAi8sy4c?si=PVkIPiHGyJgLdDTa
    A = sum(7 * 8**i for i in range(len(program) - 1)) + 1

    while True:
        res = run_program([A, 0, 0], program)

        if res == program:
            return A

        for i in range(len(res) - 1, -1, -1):
            if res[i] != program[i]:
                A += 8**i
                break


part1 = part1(data)
print(f'Part 1: {part1}')

part2 = part2(data)
print(f'Part 2: {part2}')
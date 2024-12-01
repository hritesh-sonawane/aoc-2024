#!/bin/bash

YEAR=2024

day=${1##+(0)}
if ((day < 1 || day > 25)); then
    echo "Invalid day input: $1. Must be between 1 and 25."
    exit 1
fi
# project variable is "dayXX" where XX is the day variable
project=$(printf "day%02d" $day)

if [[ -f ".session" ]]; then
  AOC_SESSION=$(<".session")
fi

if [ -z "$AOC_SESSION" ]; then
    echo "AOC_SESSION isn't set. Cannot continue lol."
    exit 1
fi
VALIDSESSION=$(curl -s "https://adventofcode.com/${YEAR}/day/1/input" --cookie "session=${AOC_SESSION}")
if [[ $VALIDSESSION =~ "Puzzle inputs differ by user." ]] || [[ $VALIDSESSION =~ "500 Internal Server" ]]; then
    echo "Invalid AOC_SESSION. Cannot continue lol."
    exit 1
fi

# a Python project directory structure
if [[ -d "${project}" ]]; then
    cd "${project}" || exit
else
    mkdir "${project}"
    cd "${project}" || exit
fi

curl -s "https://adventofcode.com/${YEAR}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

echo -n "#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
part1 = \"\"
print(f'Part 1: {part1}')

part2 = \"\"
print(f'Part 2: {part2}')" > "day${day}.py"
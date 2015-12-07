#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
lines = "".join(lines)

floor = 0
for ch in lines:
    if ch == ")":
        floor -= 1
    else:
        floor += 1

print(floor)

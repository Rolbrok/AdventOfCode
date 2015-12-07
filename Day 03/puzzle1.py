#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
lines = "".join(lines)

GRID_SIZE = 2000

grid = [[False for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]

x = y = int(GRID_SIZE / 2) 
grid[x][y] = True
n = 1

for c in lines:
    if c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    elif c == '>':
        x += 1
    elif c == '<':
        x -= 1

    if not grid[x][y]:
        n += 1
    grid[x][y] = True

print(n)

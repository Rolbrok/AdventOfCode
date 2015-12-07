#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
lines = "".join(lines)

GRID_SIZE = 2000

grid = [[False for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]

robo_x = robo_y = santa_x = santa_y = int(GRID_SIZE / 2) 
grid[robo_x][robo_y] = True
n = 1

for x, c in enumerate(lines):
    if x % 2 == 0:
        if c == '^':
            santa_y += 1
        elif c == 'v':
            santa_y -= 1
        elif c == '>':
            santa_x += 1
        elif c == '<':
            santa_x -= 1

        if not grid[santa_x][santa_y]:
            n += 1
        grid[santa_x][santa_y] = True
    else:
        if c == '^':
            robo_y += 1
        elif c == 'v':
            robo_y -= 1
        elif c == '>':
            robo_x += 1
        elif c == '<':
            robo_x -= 1

        if not grid[robo_x][robo_y]:
            n += 1
        grid[robo_x][robo_y] = True

print(n)

#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
#lines = "".join(lines)

def get(s):
    if s == "on":
        return 1
    else:
        return -1

Grid = [[0 for z in range(1000)] for i in range(1000)]

count = 0
for line in lines:
    words = line.split()
    if words[0] == "toggle":
        start_x, start_y = map(int, words[1].split(','))
        end_x, end_y = map(int, words[3].split(','))

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                Grid[x][y] += 2
                count += 2
    else:
        instruction = words[1]
        start_x, start_y = map(int, words[2].split(','))
        end_x, end_y = map(int, words[4].split(','))
        inc = get(instruction)       
 
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if inc == -1 and Grid[x][y] != 0 or inc == 1:
                    count += inc
                    Grid[x][y] += inc

print(count)
print(sum( [sum(Grid[i]) for i in range(1000)] ))

#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
#lines = "".join(lines)

def get(s):
    return (s == "on")

Grid = [[False for z in range(1000)] for i in range(1000)]

count = 0
for line in lines:
    words = line.split()
    if words[0] == "toggle":
        start_x, start_y = map(int, words[1].split(','))
        end_x, end_y = map(int, words[3].split(','))

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if Grid[x][y]:
                    count -= 1
                else:
                    count += 1
                
                Grid[x][y] = not Grid[x][y]
    else:
        instruction = words[1]
        start_x, start_y = map(int, words[2].split(','))
        end_x, end_y = map(int, words[4].split(','))
        
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if Grid[x][y] and instruction == "off":
                    count -= 1
                elif not Grid[x][y] and instruction == "on":
                    count += 1
                
                Grid[x][y] = get(instruction)

print(count)

#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

area = 0
for x, line in enumerate(lines):
    if not len(line):
        continue

    l, w, h = map(int, line.split('x'))
    area += l * w * h
    s = sorted( (l, w, h) )
    area += 2*s[0] + 2*s[1]

print(area) 

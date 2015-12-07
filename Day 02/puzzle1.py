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
    area += 2*l*w + 2*w*h + 2*h*l
    s = sorted( (l, w, h) )
    area += s[0] * s[1]

print(area) 

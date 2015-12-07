#!/usr/bin/python

import sys

lines = ""
for line in sys.stdin:
    lines += line.rstrip('\n')

floor = 0
for x, c in enumerate(lines):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    
    if floor == -1:
        print(x + 1)
        exit()

#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
lines = "".join(lines)

def md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

import hashlib

n = 0
next_str = md5(lines + str(n))
while not next_str.startswith("000000"):
    n += 1
    next_str = md5(lines + str(n))

print(n)

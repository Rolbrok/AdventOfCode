#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
#lines = "".join(lines)

def isGood(string):
    if ("ab" in string or
        "cd" in string or
        "pq" in string or
        "xy" in string):
        return 0

    vowels = 0
    rep = []
    last_c = -1
    for c in string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        if c == last_c:
            rep.append(c + c)

        last_c = c 

    if len(rep) > 0 and vowels >= 3:
        return 1
    else:
        return 0

n = 0
for i in lines:
    n += isGood(i)

print(n)

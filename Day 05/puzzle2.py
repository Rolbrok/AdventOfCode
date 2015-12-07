#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# lines as str:
#lines = "".join(lines)

def get_pairs(string):
    s = len(string)
    
    reverse = []
    pairs = []
    for i in range(0, s):
        if i + 1 >= s:
            for i in range(s-1, -1, -2):
                if i - 1 < 0:
                    break
                reverse.append(string[i - 1: i+1 :])
            break
        pairs.append(string[i: i + 2:])

    for i in reverse:
        if i not in pairs:
            pairs.append(i)

    return pairs

def isGood(string):
    pairs = get_pairs(string)
    good = 0
    nb = len(pairs)
    
    for pos, pair in enumerate(pairs):
        right = pos + 2
        for i in range(right, nb):
            if pairs[i] == pair:
                good += 1

    vowels = 0
    last_c = previous = -1
    for x, c in enumerate(string):
        if c == previous:
            vowels += 1        

        previous = last_c
        last_c = c 

    if vowels > 0 and good > 0:
        return 1
    else:
        return 0

n = 0
for i in lines:
    r = isGood(i)
    n += r

print(n)

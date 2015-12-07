#!/usr/bin/python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

results = {}
while "a" not in results:
    for l in lines:
        line = l.split()
        dest = line[-1]
        
        size = len(line) - 2
        if size == 1:
            if line[0].isdigit():
                results[dest] = int(line[0])
            elif line[0] in results:
                results[dest] = results[line[0]]
        elif size == 2:
            if line[1].isdigit():
                results[dest] = ( ~ int(line[1])) & 0xFFFF
            elif line[1] in results:
                results[dest] = ( ~ results[line[1]]) & 0xFFFF
        elif size == 3:    
            left, op, right = line[0:3:]
            
            if left.isdigit():
                left = int(left)
            elif left in results:
                left = results[left]
            else:
                continue

            if right.isdigit():
                right = int(right)
            elif right in results:
                right = results[right]
            else:
                continue

            if op == "AND":
                results[dest] = (left & right)
            elif op == "OR":
                results[dest] = (left | right)
            elif op == "LSHIFT":
                results[dest] = (left << right) & 0xFFFF
            elif op == "RSHIFT":
                results[dest] = (left >> right) & 0xFFFF

print(results["a"])

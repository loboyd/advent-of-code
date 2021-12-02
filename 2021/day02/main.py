#!/usr/bin/env python3

data = [x.strip().split(' ') for x in open('data.txt', 'r').readlines()]

# part 1
h = 0
d = 0
for m in data:
    if m[0] == 'down':
        d += int(m[1])
    elif m[0] == 'up':
        d -= int(m[1])
    elif m[0] == 'forward':
        h += int(m[1])
print(h*d)

# part 2
h = 0
d = 0
aim = 0
for m in data:
    if m[0] == 'down':
        aim += int(m[1])
    elif m[0] == 'up':
        aim -= int(m[1])
    elif m[0] == 'forward':
        h += int(m[1])
        d += int(m[1])*aim
print(h*d)

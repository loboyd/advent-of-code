#!/usr/bin/env python3

f = open("data.txt", "r")
data = [int(x.strip()) for x in f.readlines()]
f.close()

# part 1
print(sum([1 if u < v else 0 for u,v in zip(data, data[1:])]))

# part 2
data = [x+y+z for x,y,z in zip(data, data[1:], data[2:])]
print(sum([1 if u < v else 0 for u,v in zip(data, data[1:])]))

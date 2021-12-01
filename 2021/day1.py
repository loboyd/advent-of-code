#!/usr/bin/env python3

f = open("data.txt", "r")
data = [int(x.strip()) for x in f.readlines()]
f.close()

# part 1
print(sum([1 for u,v in zip(data, data[1:]) if u < v]))

# part 2
print(sum([1 for u,v in zip(data, data[3:]) if u < v]))

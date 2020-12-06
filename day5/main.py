#!/usr/bin/env python3

with open("data.txt") as f:
    data = [x.strip() for x in f.readlines()]

def getID(d):
    bin = ['0' if x == 'F' or x == 'L' else '1' for x in d]
    bin = ''.join(bin)
    bin = int(bin, 2)
    return bin

def sol1(data):
    max_id = 0
    for d in data:
        id = getID(d)
        if id > max_id:
            max_id = id
    return max_id

def sol2(data):
    s = set(list(range(1, 2**10 + 1)))
    for d in data:
        s.remove(getID(d))

    # remove low-ID seats
    id = 1
    while id in s:
        s.remove(id)
        id += 1

    # remove high-ID seats
    id = 2**10
    while id in s:
        s.remove(id)
        id -= 1

    if len(s) == 1:
        return s.pop()

if __name__ == "__main__":
    #print(sol1(data))
    print(sol2(data))


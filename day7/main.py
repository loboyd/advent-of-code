#!/usr/bin/env python3

data = open("data.txt", 'r').read().split('\n')[:-1]

def sol1(data):
    b = dict()
    for d in data:
        d = d[:-1]
        outer, inners = d.split(' contain ')

        outer = outer.rpartition(' ')[0]
        inners = inners.split(', ')
        inners = [i.rpartition(' ')[0] for i in inners]

        inners = [i.split(' ', 1)[1] for i in inners]

        for i in inners:
            if 'other' not in i:
                if i not in b:
                    b[i] = []
                b[i].append(outer)

        valid = set()
        queue = set(['shiny gold'])
        while queue:
            bag = queue.pop()
            if bag in b:
                valid.update(b[bag])
                queue.update(b[bag])

    return len(valid)

def sol2(data):
    b = dict()
    for d in data:
        d = d[:-1]
        outer, inners = d.split(' contain ')

        outer = outer.rpartition(' ')[0]
        inners = inners.split(', ')
        inners = [i.rpartition(' ')[0] for i in inners]

        inners = [i.split(' ', 1) for i in inners]

        for i in inners:
            if 'other' not in i:
                if outer not in b:
                    b[outer] = []
                b[outer].append(i)

    return count("shiny gold", b) - 1

def count(x, b):
    if x not in b:
        return 1
    contents = b[x]
    return sum(int(c[0])*count(c[1], b) for c in contents) + 1

print(sol1(data))
print(sol2(data))


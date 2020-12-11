#!/usr/bin/env python3

data = [int(x.strip()) for x in open("data.txt").readlines()]

PREAMBLE = 25

def sol1(data):
    seen = dict()
    i = 0
    while i < PREAMBLE:
        d = data[i]
        seen[d] = seen[d]+1 if d in seen else 1
        i += 1

    while i < len(data):
        d = data[i]
        seen[d] = seen[d]+1 if d in seen else 1

        valid = False
        for key in seen:
            if (d-key) in seen and seen[d-key] > 0 and seen[key] > 0 and key != d-key:
                valid = True
                break
        if not valid:
            return d

        seen[data[i-PREAMBLE]] -= 1
        i += 1

def sol2(data):
    data = data[:504]
    val = sol1(data)
    for tail in range(len(data)-1):
        for head in range(1, len(data)):
            if tail < head:
                contig = data[tail:head+1]
                if sum(contig) == val:
                    return min(contig) + max(contig)

if __name__ == "__main__":
    print(sol1(data))
    print(sol2(data))


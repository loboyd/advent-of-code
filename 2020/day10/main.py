#!/usr/bin/env python3

data = [int(x.strip()) for x in open("data.txt").readlines()]

def sol1(data):
    data = sorted(data)
    diff = [data[i+1]-data[i] for i in range(len(data)-1)]
    return (len([1 for x in diff if x == 1]) + 1) * (len([1 for x in diff if x == 3]) + 1)

def sol2(data):
    data = list(reversed(sorted(data))) + [0]
    memo = [0]*len(data)

    memo[0] = 1

    for i in range(1, len(memo)):
        for j in range(1, 4):
            if data[i] >= data[i-j] - 3:
                memo[i] += memo[i-j]

    return memo[-1]

if __name__ == "__main__":
    print(sol1(data))
    print(sol2(data))


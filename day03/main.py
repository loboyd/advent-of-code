#!/usr/bin/env python3

with open("data.txt") as f:
    data = [x.strip() for x in f.readlines()]

def sol1(data):
    ct = 0
    row = 0
    col = 0
    ncols = len(data[0])
    while row < len(data):
        if data[row][col%ncols] == '#':
            ct += 1
        row += 1
        col += 3

    return ct

def f(data, dc, dr):
    ct = 0
    row = 0
    col = 0
    ncols = len(data[0])
    while row < len(data):
        if data[row][col%ncols] == '#':
            ct += 1
        row += dr
        col += dc

    return ct

def sol2(data):
    return f(data, 1, 1)*f(data, 5, 1)*f(data, 7, 1)*f(data, 1, 2)*200

if __name__ == "__main__":
    #print(sol1(data))
    print(sol2(data))


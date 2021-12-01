#!/usr/bin/env python3

with open("data.txt") as f:
    data = [x.strip() for x in f.readlines()]

def sol1(data):
    ct = 0
    for d in data:
        d, password = d.split(':')
        password = password.strip()
        bounds, char = d.split(' ')
        low, high = bounds.split('-')
        low = int(low); high = int(high)

        if low <= sum([1 for c in list(password) if c == char]) <= high:
            ct += 1

    return ct

def sol2(data):
    ct = 0
    for d in data:
        d, password = d.split(':')
        password = password.strip()
        bounds, char = d.split(' ')
        low, high = bounds.split('-')
        low = int(low); high = int(high)

        x = password[low-1]  == char
        y = password[high-1] == char

        ct += x ^ y

    return ct

if __name__ == "__main__":
    #print(sol1(data))
    print(sol2(data))


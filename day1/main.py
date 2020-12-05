#!/usr/bin/env python3

with open("data.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]

def sol1(data):
    expenses = set()
    for d in data:
        expenses.add(d)
    for d in data:
        if (2020 - d) in expenses:
            return d*(2020-d)

def sol2(data):
    expenses = {}
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] != data[j]:
                expenses[data[i] + data[j]] = (data[i], data[j])
    for d in data:
        if (2020 - d) in expenses:
            x, y = expenses[2020-d]
            return d*x*y

if __name__ == "__main__":
    #print(sol1(data))
    print(sol2(data))


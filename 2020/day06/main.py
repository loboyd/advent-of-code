#!/usr/bin/env python3

data = [x.strip() for x in open("data.txt").readlines()]

def sol1(data):
    ct = 0
    data = '\n'.join(data)
    data = data.split('\n\n')
    for d in data:
        s = set(list(d))
        if '\n' in s:
            s.remove('\n')
        ct += len(s)

    return ct

def sol2(data):
    ct = 0
    data = '\n'.join(data)
    data = data.split('\n\n')
    s = set()
    for d in data:
        # set of chars
        s = set(list(d))
        if '\n' in s:
            s.remove('\n')

        # no of answers
        n_ans = len(d.split('\n'))

        for char in s:
            app = sum([1 for x in d if x == char])
            if app == n_ans:
                ct += 1

    return ct

if __name__ == "__main__":
    print(sol1(data))
    print(sol2(data))


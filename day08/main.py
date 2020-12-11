#!/usr/bin/env python3

data = open("data.txt").read().split('\n')[:-1]

def sol1(data):
    acc = 0
    visited = set()
    ind = 0

    while True:
        if ind in visited:
            return None
        if ind > len(data) - 1:
            return acc

        visited.add(ind)

        d = data[ind]
        op, val = d.split(' ')
        val = int(val)

        if op == 'acc':
            acc += val
            ind += 1
        elif op == 'jmp':
            ind += val
        else:
            ind += 1

    return acc


def sol2(data):
    i = 0
    while i < len(data):
        print('swapping for', i)
        d = data[i]

        # swap instructions
        op, val = d.split(' ')
        if op == 'jmp':
            op = 'nop'
        elif op == 'nop':
            op = 'jmp'
        data[i] = '{} {}'.format(op, val)


        r = sol1(data)
        print(r)
        if r is not None:
            print('val:', r)
            exit()
        else:
            print('didnt terminate')

        # swap instructions back
        if op == 'jmp':
            op = 'nop'
        elif op == 'nop':
            op = 'jmp'
        data[i] = '{} {}'.format(op, val)

        i += 1

sol2(data)


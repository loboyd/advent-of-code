#!/usr/bin/env python3

data = [x.strip() for x in open("fulldata.txt").readlines()]

def sol1(data):
    dsp = [0, 0, 0, 0]
    f = 1
    for d in data:
        direction, value = d[0], int(d[1:])
        if direction == 'F':
            dsp[f] += value
        elif direction == 'R':
            f += value//90 % 4
            f %= 4
        elif direction == 'L':
            f -= value//90 % 4
            f %= 4
        elif direction == 'N':
            dsp[0] += value
        elif direction == 'E':
            dsp[1] += value
        elif direction == 'S':
            dsp[2] += value
        elif direction == 'W':
            dsp[3] += value

    return abs(dsp[0]-dsp[2])+abs(dsp[1]-dsp[3])

def sol2(data):
    dsp = [0,  0]
    w   = [1, 10]

    for d in data:
        direction, value = d[0], int(d[1:])

        # translate ship
        if direction == 'F':
            dsp = [dsp[i]+value*w[i] for i in range(2)]

        # rotate waypoint
        elif direction == 'R' or direction == 'L':
            if value == 180:
                w = [-w[0], -w[1]]
            elif d == 'R90' or d == 'L270':
                w = [-w[1], w[0]]
            elif d == 'L90' or d == 'R270':
                w = [w[1], -w[0]]

        # translate waypoint
        elif direction == 'N':
            w[0] += value
        elif direction == 'S':
            w[0] -= value
        elif direction == 'E':
            w[1] += value
        elif direction == 'W':
            w[1] -= value

    return sum(abs(x) for x in dsp)

# Messed this up and then re-wrote to use real vectors which I subsequently
# messed up in the exact same way. Found and fixed the error and both and not
# they're both working, so I'm leaving them both
def sol2_old(data):
    dsp = [0, 0, 0, 0]
    w = [1, 10, 0, 0]
    for d in data:
        direction, value = d[0], int(d[1:])

        # move forward
        if direction == 'F':
            dsp = [dsp[i]+value*w[i] for i in range(4)]

        # rotate waypoint
        elif direction == 'R' or direction == 'L':
            if value == 180:
                w = [w[2], w[3], w[0], w[1]]
            elif d == 'R90' or d == 'L270':
                w = [w[3], w[0], w[1], w[2]]
            elif d == 'L90' or d == 'R270':
                w = [w[1], w[2], w[3], w[0]]

        # update waypoint values
        elif direction == 'N':
            w[0] += value
        elif direction == 'E':
            w[1] += value
        elif direction == 'S':
            w[2] += value
        elif direction == 'W':
            w[3] += value

    return abs(dsp[0]-dsp[2])+abs(dsp[1]-dsp[3])

if __name__ == "__main__":
    print(sol1(data))
    print(sol2(data))


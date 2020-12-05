#!/usr/bin/env python3

with open("data.txt") as f:
    data = [x.strip() for x in f.readlines()]

def sol1(data):
    ct = 0
    data = '\n'.join(data).split('\n\n')
    for pp in data:
        pp = ' '.join(pp.split('\n'))
        keys = set()
        pairs = pp.split(' ')
        for pair in pairs:
            key, _  = pair.split(':')
            keys.add(key)
        if (
            'byr' in keys and
            'iyr' in keys and
            'eyr' in keys and
            'hgt' in keys and
            'hcl' in keys and
            'ecl' in keys and
            'pid' in keys #and
            #'cid' in keys
        ):
            ct += 1

    return ct


def sol2(data):
    ct = 0
    data = '\n'.join(data).split('\n\n')
    for pp in data:
        pp = ' '.join(pp.split('\n'))
        keys = {}
        pairs = pp.split(' ')
        for pair in pairs:
            key, value  = pair.split(':')
            keys[key] = value

        if (
            'byr' not in keys or
            'iyr' not in keys or
            'eyr' not in keys or
            'hgt' not in keys or
            'hcl' not in keys or
            'ecl' not in keys or
            'pid' not in keys
        ):
            print('missing keys')
            continue

        byr = keys['byr']
        if len(byr) != 4:
            print('bad byr length')
            continue

        if int(byr) < 1920 or int(byr) > 2002:
            print('bad byr')
            continue

        iyr = keys['iyr']
        if len(iyr) != 4:
            print('bad iyr length')
            continue

        if int(iyr) < 2010 or int(iyr) > 2020:
            print('bad iyr')
            continue

        eyr = keys['eyr']
        if len(eyr) != 4:
            print('bad eyr length')
            continue

        if int(eyr) < 2020 or int(eyr) > 2030:
            print('bad eyr')
            continue

        hgt = keys['hgt']
        units = hgt[-2:]
        hgt = int(hgt[:-2])
        if units != 'cm' and units != 'in':
            print('bad unit')
            continue
        if units == 'cm' and (hgt < 150 or hgt > 193):
            print('bad height')
            continue
        if units == 'in' and (hgt < 59 or hgt > 76):
            print('bad height')
            continue

        hcl = keys['hcl']
        if hcl[0] != '#':
            print('bad color hash')
            continue

        if len(hcl) != 7:
            print('bad hcl length')
            continue

        bad = False
        for c in hcl[1:]:
            if c not in '1234567890abcdef':
                bad = True
                break
        if bad:
            bad = False
            print('bad color char')
            continue

        ecl = keys['ecl']
        if (
            ecl != 'amb' and
            ecl != 'blu' and
            ecl != 'gry' and
            ecl != 'grn' and
            ecl != 'hzl' and
            ecl != 'oth'
        ):
            print('bad ecl')
            continue

        pid = keys['pid']
        if len(pid) != 9:
            print('bad pid length')
            continue

        bad = False
        for c in pid:
            if c not in '1234567890':
                break
        if bad:
            bad = True
            print('bad pid char')
            continue

        ct += 1

    return ct

if __name__ == "__main__":
    #print(sol1(data))
    print(sol2(data))


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

def isDigit(x):
    return x in '0987123465'

def isHex(x):
    return isDigit(x) or x in 'abcdef'

def byrValid(byr):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002

def iyrValid(iyr):
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020

def eyrValid(eyr):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030

def hgtValid(hgt):
    units = hgt[-2:]
    hgt = hgt[:-2]
    if units == 'in':
        if len(hgt) == 2 and isDigit(hgt[0]) and isDigit(hgt[1]):
            if 59 <= int(hgt) <= 76:
                return True
    elif units == 'cm':
        if len(hgt) == 3 and isDigit(hgt[0]) and isDigit(hgt[1]) and isDigit(hgt[2]):
            if 150 <= int(hgt) <= 193:
                return True
    return False

def hclValid(hcl):
    return (
        len(hcl) == 7 and
        hcl[0] == '#' and
        isHex(hcl[1]) and 
        isHex(hcl[2]) and 
        isHex(hcl[3]) and 
        isHex(hcl[4]) and 
        isHex(hcl[5]) and 
        isHex(hcl[6])
    )

def eclValid(ecl):
    return (
        ecl == 'amb' or
        ecl == 'blu' or
        ecl == 'brn' or
        ecl == 'gry' or
        ecl == 'grn' or
        ecl == 'hzl' or
        ecl == 'oth'
    )

def pidValid(pid):
    return (
        len(pid) == 9   and
        isDigit(pid[1]) and 
        isDigit(pid[2]) and 
        isDigit(pid[3]) and 
        isDigit(pid[4]) and 
        isDigit(pid[5]) and 
        isDigit(pid[6]) and 
        isDigit(pid[7]) and 
        isDigit(pid[8])
    )

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
            'byr' in keys and byrValid(keys['byr']) and
            'iyr' in keys and iyrValid(keys['iyr']) and
            'eyr' in keys and eyrValid(keys['eyr']) and
            'hgt' in keys and hgtValid(keys['hgt']) and
            'hcl' in keys and hclValid(keys['hcl']) and
            'ecl' in keys and eclValid(keys['ecl']) and
            'pid' in keys and pidValid(keys['pid'])
        ):
            ct += 1

    return ct

if __name__ == "__main__":
    #print(sol1(data))
    print(sol2(data))


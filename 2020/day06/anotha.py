#!/usr/bin/env python3

# stolen from some Redditor

print(sum(len(set.union(*map(set, g.split('\n')))) for g in open('data.txt').read().split('\n\n')))
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in open('data.txt').read().split('\n\n')))


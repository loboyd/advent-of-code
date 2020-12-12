#!/usr/bin/env python3

data = [x.strip() for x in open("data.txt").readlines()]

def step(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    new = [['.']*ncols for _ in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            neighbors = [row[max(j-1,0):min(j+2,ncols)] for row in grid[max(i-1,0):min(nrows,i+2)]]
            nocc = sum([1 for row in neighbors for seat in row if seat=='#'])

            if grid[i][j] == 'L':
                new[i][j] = '#' if nocc < 1 else 'L'

            if grid[i][j] == '#':
                new[i][j] = 'L' if nocc >= 5 else '#'

    return new

DIRECTIONS = [
    ( 1,  0),
    ( 1,  1),
    ( 0,  1),
    (-1,  1),
    (-1,  0),
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
]

def step2(grid, r=False):
    nrows = len(grid)
    ncols = len(grid[0])

    occ = set()
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == '#':
                occ.add((i,j))

    new = [['.']*ncols for _ in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            nocc = 0

            for dr, dc in DIRECTIONS:
                (ii, jj) = (i, j)
                while 0 <= ii < nrows and 0 <= jj < ncols:
                    if (ii, jj) != (i, j):
                        if grid[ii][jj] == '#':
                            nocc += 1
                            break
                        elif grid[ii][jj] == 'L':
                            break
                    ii += dr
                    jj += dc

            if grid[i][j] == 'L':
                new[i][j] = '#' if nocc == 0 else 'L'

            if grid[i][j] == '#':
                new[i][j] = 'L' if nocc >= 5 else '#'

            if r and grid[i][j] != '.':
                new[i][j] = str(nocc)

    return new

def sol1(data):
    grid = [list(row) for row in data]
    new = step(grid)
    while new != grid:
        grid = new
        new = step(grid)

    return sum(1 for row in new for seat in row if seat=='#')

def sol2(data):
    grid = [list(row) for row in data]
    new = step2(grid)

    while new != grid:

        grid = new
        new = step2(grid)

    return sum(1 for row in new for seat in row if seat=='#')

if __name__ == "__main__":
    print(sol1(data))
    print(sol2(data))


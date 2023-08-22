import numpy as np


grid = np.zeros((1000,1000), dtype=bool)

with open('input06.txt') as fp:
    inp = fp.read().split('\n')


def parse_coord(s):
    return (int(i) for i in s.split(','))


for line in inp:
    words = line.split(' ')
    l, t = parse_coord(words[-3])
    r, b = parse_coord(words[-1])
    if line.startswith("turn on"):
        grid[t:b+1, l:r+1] = True
    elif line.startswith("turn off"):
        grid[t:b+1, l:r+1] = False
    elif line.startswith("toggle"):
        grid[t:b+1, l:r+1] = ~grid[t:b+1, l:r+1]

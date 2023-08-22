import numpy as np

def parse_coord(s):
    return (int(i) for i in s.split(','))

with open('input06.txt') as fp:
    inp = fp.read().strip().split('\n')


grid = np.zeros((1000,1000), dtype=int)
for line in inp:
    words = line.split(' ')
    l, t = parse_coord(words[-3])
    r, b = parse_coord(words[-1])
    if line.startswith("turn on"):
        grid[t:b+1, l:r+1] += 1
    elif line.startswith("turn off"):
        grid[t:b+1, l:r+1] -= -1
    elif line.startswith("toggle"):
        grid[t:b+1, l:r+1] += 2

    grid = np.clip(grid, 0, None)

print(np.sum(grid))

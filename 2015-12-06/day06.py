import numpy as np


grid = np.zeros((1000,1000))

with open('input06.txt') as fp:
    inp = fp.read().split('\n')


def parse_coord(s):
    return (int(i) for i in s.split(','))


for line in inp:
    words = line.split(' ')
    l, t = parse_coord(words[-3])
    r, b = parse_coord(words[-1])
    if line.startswith("turn on"):
        pass
    elif line.startswith("turn off"):
        pass
    elif line.startswith("toggle"):
        pass

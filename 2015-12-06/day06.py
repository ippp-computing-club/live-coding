import numpy as np


grid = np.zeros((1000,1000))

with open('input06.txt') as fp:
    inp = fp.read().split('\n')


for line in inp:
    if line.startswith("turn on"):
        pass
    elif line.startswith("turn off"):
        pass
    elif line.startswith("turn toggle"):
        pass

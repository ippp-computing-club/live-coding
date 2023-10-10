a = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}  #1
coords = set([(0,0)]) # set takes an iterable               #2
with open("input.txt") as f: dat = f.read().strip()         #3
n = 2
for i in range(n):                                          #4
    xs = ys = 0                                             #5
    for char in dat[i::n]: # every even                     #6                                         #9
        coords.add((xs:=xs+a[char][0], ys:=ys+a[char][1]))  #7
print(len(coords))                                          #8

import numpy as np

file = open("input.txt", "r")
data = file.read().strip()

# dictionary for symbols in input
symbols = {
    "^": (0,1),
    "v": (0,-1),
    ">": (1,0),
    "<": (-1,0)
}

# function to increase/decrease x and y
def coor_update(sym,x,y,dictio):
    """
    if sym == "^":
        y = y + 1
    elif sym == "v":
        y = y - 1
    elif sym == ">":
        x = x + 1
    elif sym == "<":
        x = x - 1
    """
    x += symbols[sym][0]
    y += symbols[sym][1]

    if (x,y) not in dict_coor:
        dict_coor[(x,y)] = 1

    return x,y,dict_coor

x_s = 0
y_s = 0
x_r = 0
y_r = 0

dict_coor = {(x_s,y_s):1}


for n,i in enumerate(data):
    if n % 2 == 0:
        x_s += symbols[i][0]
        y_s += symbols[i][1]

        if (x_s,y_s) not in dict_coor:
            dict_coor[(x_s,y_s)] = 1
    else:
        x_r += symbols[i][0]
        y_r += symbols[i][1]

        if (x_r,y_r) not in dict_coor:
            dict_coor[(x_r,y_r)] = 1
"""
for step in data[0::2]:
    x_s += symbols[step][0]
    y_s += symbols[step][1]

    if (x_s,y_s) not in dict_coor:
        dict_coor[(x_s,y_s)] = 1
    

for step in data[1::2]:
    x_r += symbols[step][0]
    y_r += symbols[step][1]

    if (x_r,y_r) not in dict_coor:
        dict_coor[(x_r,y_r)] = 1
"""

N = len(dict_coor.keys())
print("Total number of houses visited is:", N)

file.close()

"""
#N = 1
#coordinates = []
#coordinates.append((x_s,y_s))
#instructions = []

for i in data:
    if i == "^":
        y = y + 1
        if (x,y) not in coordinates:
            coordinates.append((x,y))
            N += 1
    elif i == "v":
        y = y - 1
        if (x,y) not in coordinates:
            coordinates.append((x,y))
            N += 1
    elif i == ">":
        x = x + 1
        if (x,y) not in coordinates:
            coordinates.append((x,y))
            N += 1
    elif i == "<":
        x = x - 1
        if (x,y) not in coordinates:
            coordinates.append((x,y))
            N += 1

        if i == "^":
            y_s = y_s + 1
            if (x_s,y_s) not in coordinates:
                N += 1
        elif i == "v":
            y_s = y_s - 1
            if (x_s,y_s) not in coordinates:
                N += 1
        elif i == ">":
            x_s = x_s + 1
            if (x_s,y_s) not in coordinates:
                N += 1
        elif i == "<":
            x_s = x_s - 1
            if (x_s,y_s) not in coordinates:
                N += 1
 
        x_s, y_s = coor_update(i,x_s,y_s)

        if (x_s,y_s) not in dict_coor: #coordinates:
            #coordinates.append((x_s,y_s))
            dict_coor[(x_s,y_s)] = 1

        x_s, y_s, dict_coor = coor_update(i,x_s,y_s,dict_coor)
"""


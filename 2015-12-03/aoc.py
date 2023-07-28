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
def coor_update(sym,x,y):
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

    return x,y

#N = 1

#coordinates = []

x_s = 0
y_s = 0
x_r = 0
y_r = 0
#coordinates.append((x_s,y_s))
dict_coor = {(x_s,y_s):1}

#instructions = []

for n,i in enumerate(data):
    if n % 2 == 0:
        """
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
        """
        
        x_temp = x_s
        y_temp = y_s
        x_s, y_s = coor_update(i,x_s,y_s)

        if (x_s,y_s) not in dict_coor: #coordinates:
            #coordinates.append((x_s,y_s))
            dict_coor[(x_s,y_s)] = 1
    else:
        """
        if i == "^":
            y_r = y_r + 1
            if (x_r,y_r) not in coordinates:
                N+= 1
        elif i == "v":
            y_r = y_r - 1
            if (x_r,y_r) not in coordinates:
                N += 1
        elif i == ">":
            x_r = x_r + 1
            if (x_r,y_r) not in coordinates:
                N += 1
        elif i == "<":
            x_r = x_r - 1
            if (x_r,y_r) not in coordinates:
                N += 1
        """
        x_r, y_r = coor_update(i,x_r,y_r)

        if (x_r,y_r) not in dict_coor: #coordinates:
            #coordinates.append((x_r,y_r))
            dict_coor[(x_r,y_r)] = 1       

"""
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
"""

N = len(dict_coor.keys())#len(coordinates)
print("Total number of houses visited is:", N)

file.close()

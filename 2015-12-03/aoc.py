import numpy as np

file = open("aocinput.txt", "r")
data = file.read().strip()

N = 1

coordinates = []

x_s = 0
y_s = 0
x_r = 0
y_r = 0
coordinates.append((x_s,y_s))

instructions = []

for n,i in enumerate(data):
    if n % 2 == 0:
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
        coordinates.append((x_s,y_s))
    else:
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
        coordinates.append((x_r,y_r))
                
    
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

print("Total number of houses visited is:", N)



file.close()

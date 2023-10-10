file = open("input.txt", "r")
data = file.read().strip()

#function to move santa to new house
def movement(move,xpos,ypos):
    if move == "^":
        ypos = ypos + 1
    elif move == "v":
        ypos = ypos - 1
    elif move == ">":
        xpos = xpos + 1
    elif move == "<":
        xpos = xpos - 1
    return(xpos,ypos)

#function to keep track of houses visited
def houses_visited(visited,pos):
    if pos not in visited:
        visited.append(pos)

diff_houses = [(0,0)]

x_s = 0
y_s = 0


for step in data:
    x_s,y_s = movement(step,x_s,y_s)
    houses_visited(diff_houses,(x_s,y_s))


print("Total number of houses visited is:", len(diff_houses))

diff_houses = [(0,0)]

x_s = 0
y_s = 0
x_r = 0
y_r = 0


for step in data[0::2]:
    x_s,y_s = movement(step,x_s,y_s)
    houses_visited(diff_houses,(x_s,y_s))
    

for step in data[1::2]:
    x_r,y_r = movement(step,x_r,y_r)
    houses_visited(diff_houses,(x_r,y_r))
    

print("The next year, total number of houses visited is:", len(diff_houses))

file.close()
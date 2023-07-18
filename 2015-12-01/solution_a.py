"""
Solution for 2015-12-01 advent of code
part (a)
"""

# read the file

file = open("input.txt", "r")
instructions = file.read()

# print(instructions, "\n")
# print(instructions[0])

total = 0

for x in instructions:
    if x == "(":
        total += 1
    elif x == ")":
        total -= 1

print(total)

"""
Solution for 2015-12-01 advent of code
part (b)
"""

# read the file

file = open("input.txt", "r")
instructions = file.read()

total = 0

for idx, x in enumerate(instructions):
   if x == "(":
       total += 1
   elif x == ")":
       total -= 1
       if total < 0:
           print(idx+1)
           break


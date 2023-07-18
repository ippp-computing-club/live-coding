
total_wrap = 0
total_ribbon = 0

in_file = open("input.txt",'r')

lines = in_file.readlines()
for line in lines:
    numbers = line.strip().split("x")
    l = float(numbers[0])
    w = float(numbers[1])
    h = float(numbers[2])

    # wrap
    area = 2*l*w + 2*w*h + 2*h*l

    min_area = min(l*w , w*h , l*h)

    total_wrap += area + min_area

    # ribbon
    bow = l*w*h
    perimeter = min(2*(l+h) , 2*(l+w), 2*(w+h))

    total_ribbon += perimeter + bow

print(total_wrap)
print(total_ribbon)
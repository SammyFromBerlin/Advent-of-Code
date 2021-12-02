import os

h = 0
d = 0
aim = 0
with open("2.txt") as file:
    list = file.readlines()
    for i in list:
        direction = i.split(" ")[0]
        units = int(i.split(" ")[1])
        if direction == "forward":
            h += units
            d = d + (aim * units )
        elif direction == "down":
            aim += units
        elif direction == "up":
            aim -= units
result = h * d
print(str(h))
print(str(d))
print(str(result))

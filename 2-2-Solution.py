import os

h = 0
d = 0
aim = 0
with open("2.txt") as file:
    list = file.readlines()
    for i in list:
       if str(i[0]) == "f":
           tmp = i.split(" ")[1][0]
           h += int(tmp)
           d = d + (aim * int(tmp))
       elif str(i[0]) == "d":
          tmp = i.split(" ")[1][0] 
          aim += int(tmp)
       elif str(i[0]) == "u":
           tmp = i.split(" ")[1][0]
           aim -= int(tmp)
           
    result = h * d
print(str(h))
print(str(d))
print(str(result))

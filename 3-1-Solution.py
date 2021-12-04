import os

taskfile = open("3.txt").readlines()

# list for adding column most common bit
gRate = []
eRate = []
zero = one = k = 0

#print(len(taskfile[0]))

# range from 0 to 11: for every column
for l in range(0,len(taskfile[0])-1):
    for element in taskfile:
        if element[k] == "0":
            zero += 1
        else:
            one += 1
    if zero < one:
        gRate.append("1")
        eRate.append("0")
    else:
        gRate.append("0")
        eRate.append("1")
    zero = 0
    one = 0
    k+= 1
#concatinating each elemnt to get string
# bin to int 
print(gRate)
print(eRate)
voidString = ""
gRate = voidString.join(gRate)
print(gRate)
g = int(gRate,2)
eRate = voidString.join(eRate)
e = int(eRate,2)

result = g * e
print(result)
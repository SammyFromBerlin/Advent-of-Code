import os

taskfile = open("3.txt").readlines()
taskfileTwo = open("3.txt").readlines()

# help variables
tempOne = []
tempZero = []
oxygenRate = []
co2Rate = []
zero = one = k = m = 0

# range from 0 to 11: for every column
for l in range(0,12):
    for element in taskfile:
        #seperating elements 
        if element[k] == "0":
            zero += 1
            tempZero.append(element)
        else:
            one += 1
            tempOne.append(element)
    #checking whether more 0 or 1
    if zero > one:
        taskfile = tempZero
    elif zero < one:
        taskfile = tempOne
    else:
        taskfile = tempOne
    #empty all
    tempOne = []
    tempZero = []
    zero = 0
    one = 0
    k+= 1

for j in range(0,12):
    for co2 in taskfileTwo:
        if co2[m] == "0":
            zero += 1
            tempZero.append(co2)
        else:
            one += 1
            tempOne.append(co2)
    # stop on last element
    if len(taskfileTwo) == 1:
        break
    elif zero > one:
        taskfileTwo = tempOne
    elif zero < one:
        taskfileTwo = tempZero
    
    else:
        taskfileTwo = tempZero
    
    tempOne = []
    tempZero = []
    zero = 0
    one = 0
    m+= 1
    
# removing \n and convert bin to dec
oxygenRate = taskfile
co2Rate = taskfileTwo
print(oxygenRate)
print(co2Rate)
voidString = ""

oxygenRate = voidString.join(oxygenRate)
o = int(oxygenRate,2)

co2Rate = voidString.join(co2Rate)
co2 = int(co2Rate,2)

result = o * co2
print(result)
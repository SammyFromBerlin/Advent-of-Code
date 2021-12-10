import numpy as np
import os


#modified txt file for easier read
with open('5.txt', 'r') as file:
    data = file.read()

line_arr = data.split('\n')

matrix = np.zeros((1000,1000), dtype=int)

for i in range(len(line_arr)):
    line = line_arr[i].split(" ")
    firstPoint = line[0].split(",")
    secondPoint = line[1].split(",")
    #x = COLUMN y = ROW
    x1, y1  = int(firstPoint[0]),int(firstPoint[1])

    x2, y2 = int(secondPoint[0]),int(secondPoint[1])
    # Changing only elements on row
    if y1 == y2:
        # checking "downwards" on matrix
        if x1 < x2:
            for i in range(x1,x2+1):
                # SAME ROW, only increase column element
                matrix[y1,i] += 1
        # checking upwards
        else:
            for i in range(x2,x1+1):
                # SAME ROW, only increase column element
                matrix[y1,i] += 1
    #changing
    elif x1 == x2:
        # checking "downwards" on matrix
        if y1 < y2:
            for j in range(y1,y2+1):
                matrix[j,x1] += 1
        # checking upwards
        else:
            for j in range(y2,y1+1):
                matrix[j,x1] += 1
                
# counting all matrix elements >= 2
result = 0
for i in range(len(matrix)):
    for k in range(len(matrix)):
        if matrix[i,k] >= 2:
            result += 1
print(result)
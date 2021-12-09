import numpy as np
from numpy.lib import arrayterator
from numpy.lib.function_base import delete
import sys

testArray = np.loadtxt("4.txt", dtype= int)
drawnNumbers = [90,4,2,96,46,1,62,97,3,52,7,35,50,28,31,37,74,26,59,53,82,47,83,80,19,40,68,95,34,55,54,73,12,78,30,63,57,93,72,77,56,91,23,67,64,79,85,84,76,10,58,0,29,13,94,20,32,25,11,38,89,21,98,92,42,27,14,99,24,75,86,51,22,48,9,33,49,18,70,8,87,61,39,16,66,71,5,69,15,43,88,45,6,81,60,36,44,17,41,65]

arr = testArray.reshape(100,5,5)
firstBingo = []
lastBingo = []

first = 0
second = 0
#iterate through all drawn numbers
for num in drawnNumbers:
    #iterate through list
    for i in range(0,len(arr)):
        arr = np.where(num == arr, -1, arr)
        # after chaning matrices elements going through all to check if bingo
        for j in range(0,len(arr)):
            # Part 2: if last element is found calculate everything and stop
            if len(arr) == 1 and (any(np.sum(arr[j], axis=0) == -5) or any(np.sum(arr[j], axis=1) == -5)):
                second = num 
                lastBingo.append(arr[j])
                print(first)
                print(firstBingo[0])
                
                print(second)
                print(lastBingo[0])
                endResult = np.sum(np.where(-1==firstBingo[0], 0, firstBingo[0]))
                endResultTwo = np.sum(np.where(-1==lastBingo[0], 0, lastBingo[0]))
                result = endResult * first
                resultTwo = endResultTwo * second
                print(str(result))
                print(str(resultTwo))
                sys.exit()
            # Part 1 : get first matrix to bingo  
            elif len(firstBingo) == 0 and (any(np.sum(arr[j], axis=0) == -5) or any(np.sum(arr[j], axis=1) == -5)):
                firstBingo.append(arr[j])
                arr = np.delete(arr, j, 0)
                first = num
                break
            # check if current matrix has bingo and delete
            elif any(np.sum(arr[j], axis=0) == -5) or any(np.sum(arr[j], axis=1) == -5):
                arr = arr = np.delete(arr, j, 0)
                break
        


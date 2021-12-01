import os 

with open("1-1.txt") as file:
    #print(file.readlines())
    #print(type(file.read()))
    liste = file.readlines()
    currEle = int(liste[0])
    v = 0
    for i in liste:
        tmp = int(i)
        if currEle < tmp :
            v += 1
        currEle = tmp
    print(str(v))

    
    

import os 

with open("1-1.txt") as file:
    liste = file.readlines()
    a = int(liste[0])
    b = int(liste[1])
    c = int(liste[2])
    currTripleResult = a+b+c
    result = 0
    for i in range(3, len(liste)):
        x = int(liste[i-2])
        y = int(liste[i-1])
        z = int(liste[i])

        currTripleView = x+y+z

        if currTripleResult < currTripleView:
            result += 1
        currTripleResult = currTripleView

    print(str(result))
    


    

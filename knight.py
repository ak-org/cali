import random
import statistics

def knightmove(startSquare):
    if startSquare == 0:
       move = [9, 6]
    elif startSquare == 1:
       move = [7, 8, 10]
    elif startSquare == 2:
       move = [4, 9, 11]
    elif startSquare == 3:
       move = [4, 9, 11]
    elif startSquare == 4:
       move = [2, 10, 13]
    elif startSquare == 5:
       move = [3, 11, 12, 14]
    elif startSquare == 6:
       move = [0, 8, 13, 15]
    elif startSquare == 7:
       move = [1, 9, 14]
    elif startSquare == 8:
       move = [1, 6, 14]
    elif startSquare == 9:
       move = [0, 2, 7, 15]
    elif startSquare == 10:
       move = [1, 3, 4, 12]
    elif startSquare == 11:
       move = [2, 5, 13]
    elif startSquare == 12:
       move = [5, 10]
    elif startSquare == 13:
       move = [4, 6, 11]
    elif startSquare == 14:
       move = [5, 7, 8]
    elif startSquare == 15:
           move = [6,9]   
    moveto = move[random.randrange(0, len(move), 1)]
    #print("Knigt Moves from ", startSquare, " to ", moveto, len(move))
    return moveto         


                       

def eval16(f):
    seed = 0
    T = 16
    S = []
    modulo1 = 13
    returnedSquare = knightmove(seed)
    S.append(returnedSquare)
    for i in range(1,T):
        returnedSquare = knightmove(returnedSquare)
        S.append(returnedSquare)
    #print(S)
    #print("length , Sum ", len(S), sum(S))  
    if f == 1: 
        print('Mean : {0:.10f}'.format((sum(S) % modulo1) / T))
        print('Stdev : {0:.10f}'.format(statistics.stdev(S)))
    return S


def eval512(f):
    seed = 0
    T = 512
    S = []
    modulo2 = 311
    returnedSquare = knightmove(seed)
    S.append(returnedSquare)
    for i in range(1, T):
        returnedSquare = knightmove(returnedSquare)
        S.append(returnedSquare)
    if f == 1:
        #print("length , Sum ", len(S), sum(S))
        print('Mean : {0:.10f}'.format((sum(S) % modulo2) / T))
        print('Stdev : {0:.10f}'.format(statistics.stdev(S)))
    return S

def prob16():
    count5 = 0
    count13 = 0
    for i in range(0,10000):
        ret = eval16(0)
        ret = sum(ret)
        
        if ret % 13 == 0:
            count13 +=  1
            if ret % 5 == 0:
                    count5 += 1
    if count13 != 0:
        print("prob =  {0:.10f}".format(count5 / count13))


def prob512():
    count43 = 0
    count7 = 0
    for i in range(0, 10000):
        ret = eval512(0)
        ret = sum(ret)

        if ret % 43 == 0:
            count43 += 1
            if ret % 7 == 0:
                    count7 += 1
    if count7 != 0:
        print("Prob =  {0:.10f}".format(count7 / count43))
    
print(" == T is 16 == ")   
eval16(1)
print(" == T is 512 == ")
eval512(1)
print(" == T is 16 == ")
prob16()
print(" == T is 512 == ")
prob512()

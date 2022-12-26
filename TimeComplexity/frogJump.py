def solution(X, Y, D):
    i = 0
    while(Y - X > 0):
        X = X + D
        i = i + 1
  
    return(i)
    pass

import math 
def solution2(X, Y, D):

    i = (Y-X)/D 
    i = math.ceil(i)
    return(i)
    pass

print(solution2(10,85,30))
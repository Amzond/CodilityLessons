

import sys
def solution(A):
    
    mini = sys.maxsize
    for i in range(len(A)):
        if(i+1 not in A):
            if(mini > i+1):
                mini = i + 1
        if (i+2 > len(A)):
            if(mini > i+2):
                mini = i + 2
    
    return mini

def solution2(A):
    
    mini = 1
    A.sort()
    for i in range(len(A)):
        if(A[i] == mini ):
            mini = mini + 1
        
    
    return mini



A = [1,3,6,4,1,2]
print(solution2(A))
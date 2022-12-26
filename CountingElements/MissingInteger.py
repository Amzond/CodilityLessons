# first solution
# O(N^2)
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
    
    print(mini)
    return mini

    pass


A = [1,3,6,4,1,2,8]
B = [1,2,3]
solution(A)
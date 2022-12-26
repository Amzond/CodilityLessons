
 # sort and take bigest numbers 
import sys
def solution(A):
    maxi = sys.maxsize
    A.sort() 
    print(A)
    p1 = A[0] * A[1] * A[-1] # if all positive 
    p2 = A[-3] * A[-2] * A[-1]  # if negative too
    maxi = max(p1, p2)
    return maxi
    pass

A = [-3,1,2,-2,5,6]
#A = [-9, -8, -7, -6, -5, -4, -3, -2, -1]
print(solution(A))
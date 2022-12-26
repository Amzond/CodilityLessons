
# bad performance 
import sys
def solution(A):
    min = sys.maxsize
    diff = 0
    for i in range(1,len(A)):
        diff = abs(sum(A[0:i])-sum(A[i:len(A)]))
        if (min > diff):
            min = diff
    return min

# O(n) should be good performance
def solution2(A):
    min = sys.maxsize
    diff = 0
    sum_all = sum(A)
    temp = A[0]
    sum_all = sum_all - temp 
    for i in range(1,len(A)):
        diff = abs(temp - sum_all)
        sum_all = sum_all - A[i]
        temp = temp + A[i]
        
        if (min > diff):
            min = diff
    return min


A = [3,1,2,4,3]
print(solution2(A))
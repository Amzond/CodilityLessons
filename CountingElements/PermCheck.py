
# first O(N^2)
def solution(A):
    pre = 0
    temp = 0
    for i in range(len(A)):
        if(i+1 in A ):
            temp = temp + 1
    if( temp == len(A)):
        pre = 1
    return pre

# nd O(N log N) but... its works if data starts from 1
def solution2(A):
    pre = 0
    temp = 0
    A.sort()
    print(A)
    for i in range(len(A)):
        if(A[i] == i + 1 ):
            temp = temp + 1
    if( temp == len(A)):
        pre = 1
    return pre
A = [4,1,2,3]
print(solution2(A))
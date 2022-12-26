
def solution(A):
    temp = {}
    for i in range(len(A)):
        temp[A[i]] = A[i]

    return len(temp)
    pass

A = [2,1,1,2,3,1]
print(solution(A))
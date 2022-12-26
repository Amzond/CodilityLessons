

def solution(A):
    temp = 0
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            temp = temp + 1
        else:
            count = count + temp
        if (count > 1000000000):
            return -1
    return count


A = [0,1,0,1,1]
print(solution(A))
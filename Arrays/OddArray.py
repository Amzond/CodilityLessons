import operator as op

def solution(A):
  
    for i in range(len(A)):
        if(op.countOf(A,A[i]) % 2 != 0):
            return(A[i])
    pass


A = [9,3,9,3,9,7,9]
print(solution(A))


def solution(A):
    odd_count = 0
    
    for i in (range(len(A))):
        if( A[i] % 2 != 0):
            odd_count = odd_count + 1
    if( len(A) / 2 == odd_count ):
        return True
    
    return False
    pass

A = [2,7,4,6,3,1]
A = [2,-1]

print(solution(A))
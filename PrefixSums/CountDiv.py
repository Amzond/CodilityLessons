
# Correct but bad performance :/
def solution(A, B, K):
    
    count = 0

    for i in range(A,B+1):
        if( i%K == 0):
            count = count + 1
    return count




A = 6
B = 11 
K = 2
print(solution(A,B,K))
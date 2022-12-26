
# first solution
def solution(N, A):
    
    B = [0] * (N)
    
    for i in range(len(A)):
        if(A[i] <= N):
            B[A[i]-1] += 1
        elif( A[i] == N +1):
            B = [max(B)] * (N)

            
    print(B)
    
    pass

# nd solution 
def solution2(N, A):
    
    B = [0] * (N)
    maxi = 0
    for i in range(len(A)):
        if(A[i] <= N):
            B[A[i]-1] += 1
            
            if(B[A[i]-1] > maxi):
                maxi = B[A[i]-1]
        elif( A[i] == N +1):
            B = [maxi] * (N)

    print(B)

    pass

A = [3,4,4,6,1,4,4]
N = 5
solution2(N,A)
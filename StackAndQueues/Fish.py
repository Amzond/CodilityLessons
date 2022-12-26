def solution(A, B):
    
    alive = 0
    tempB = []
    for i in range(len(A)):
        
        
        if B[i] == 1:
            tempB.append(A[i])
            continue
            
        while tempB:
            if( tempB[-1] > A[i]):
                break
            tempB.pop()

        else:
            alive = alive + 1        
           
    alive = alive + len(tempB)
    return  alive
    pass


A = [4,3,2,1,5]
B = [0,1,0,0,0]

print(solution(A,B))
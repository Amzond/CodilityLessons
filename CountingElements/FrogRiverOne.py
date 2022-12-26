

def solution(X, A):
    
    sek = -1
    temp = {}
    for i in range(len(A)):
        temp[A[i]] = i
        print(temp)
        if (len(temp) == X ):
            sek = i
            break
    return sek  
    pass



A = [1,3,1,4,2,3,5,4]
X = 5
print(solution(X,A))

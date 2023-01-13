

def solution(A):
    
    count = 0
    tempA = [] 
    maxi = 0
    maxi2 = 0
    answ = 0
    tempString = ""
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i].count(A[i][j]) == 1:
                tempA.append(A[i])
                
    for i in range(len(tempA)):
        lenn = len(tempA[i])
        if lenn > maxi:
            maxi = lenn
            tempString = A[i]
    
    for i in range(len(tempA)):
        lenn = len(tempA[i])
        print(tempString)
        if lenn > maxi2 and tempString != A[i]:
            maxi2 = lenn
            tempString = A[i]
    
    answ = maxi + maxi2
    
    return answ         
    
    pass


def solution2(A):
    
    count = 0
    indexArray = []
    for i in A:
        print(set(i))
        if(len(set(i)) != len(i)):
            A.pop(count)
        count += 1
    print(A)
    
    pass



def solution3(A):
    
    temp = ""
    maxi = 0
    tempA = {}
    for i in range(len(A)-1):
        temp = A[i] + A[i+1]
        for j in temp:
            if j in temp:
                tempA[j] = j
            if( len(tempA) == len(temp) and maxi < len(tempA) ):
                maxi = len(tempA)
        tempA = {}
    
    return maxi
    
    
A = ["co","dil", "ity"]
A = ["co", "dil", "yyy"]
A = ["phone", "smart", "i", "mobile"]
print(solution3(A))
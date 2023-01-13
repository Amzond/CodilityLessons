
# O(N^2)
def solution(A):
    
    maxi = 0
    temp = 0
    for i in range(len(A)):
        for j in range(i,len(A)-1):
            temp = A[j+1] - A[i]
            if ( temp > maxi):
                maxi = temp

    return maxi
    
    pass


def solution2(A):
    
    max_slice = 0
    
    for i in range(len(A)-1):
        element = max(A[i+1:]) # bad performance bcs array
        if(element - A[i] > max_slice):
            max_slice = element - A[i]

    return max_slice
    
    pass

def solution3(A):
    
    if len(A) == 0:
        return 0
    max_slice = 0
    for i in range(len(A)):
        temp = A[i+1:]
        temp.sort() 
        if( len(temp) != 0):
            element = temp.pop()
            if(element - A[i] > max_slice):
                max_slice = element - A[i]       
    

    return max_slice
    

def solution4(A):
    max_profit = 0
    min_price = A[0] 
    
    for i in range(1,len(A)):
        max_profit = max( max_profit, A[i] - min_price )
        min_price = min( min_price, A[i] )

    return max_profit
    

A = [23171, 21011, 21123, 21366, 21013, 21367]
#A = [1, 6, 15, 5]
print(solution4(A))
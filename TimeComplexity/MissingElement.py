

# first solution 
def solution(A):
    
    for i in range(len(A)):
        if( i+1 not in A):
            return i+1
    pass

# 2nd solution
def solution2(A):    
    i = (len(A)+1) * (len(A)+ 2)//2
    i = i - sum(A) 
    return i 
    
A = [1,3,6,4,1,2]
print(solution2(A))
def solution(N):

    binary = format(N,'b')
    print(binary)
    maxi = 0
    curr = 0  
    for i in range(binary.__len__()):
        if int(binary[i]) == 0 :
            curr = curr + 1
            
        elif int(binary[i]) == 1:
            if( curr > maxi):
                maxi = curr
            
            curr = 0        
    return maxi
    
    
print(solution(74901729))

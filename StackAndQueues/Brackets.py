

# 50%
def solution(S):
    
    if (len(S) % 2 != 0):
        return 0
    half = len(S) // 2
    f_half = S[:half]
    s_half = S[half:]
    s_half = s_half[::-1]
    temp = 0
    for i in range(half):
        if(f_half[i] == "{" and s_half[i] == "}"):
            temp = temp + 1
        elif(f_half[i] == "[" and s_half[i] == "]"):
            temp = temp + 1
        elif(f_half[i] == "(" and s_half[i] == ")"):
            temp = temp + 1
        elif(f_half[i] == ")" and s_half[i] == "(" and half > 1 ):
            temp = temp + 1
            
    if temp == half:
        return 1
    else: 
        return 0
            

def solution2(S):
    temp = 0
    if (len(S) % 2 != 0):
        return temp
    
    symbols = {"]":"[","}":"{", ")":"("}
    arr = []
    for i in range(len(S)):
        if S[i] == "[" or S[i] == "{" or S[i] == "(":
            arr.append(S[i])
        elif (len(arr) == 0):
            return temp
        else:
            if symbols[S[i]] != arr.pop():
                return temp
    return 1

  
S = "{[()()]}"
S = ")("
print(solution2(S))

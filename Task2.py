

def solution(S):
    count = 0
    if S[0] == "B" and S[len(S) - 1] == "A":
        a_count = 0
        b_count = 0
        for i in range(len(S)):
            if S[i] == "A":
                a_count += 1
            else:
                b_count += 1
        if a_count > b_count:
            return b_count
        else:
            return a_count
    else:
        last_a_index = 0
        deleted_b = 0
        for i in range(len(S)):
            if S[i] == "A":
                last_a_index = i
        for i in range(last_a_index):
            if S[i] == "B":
                deleted_b += 1
        return deleted_b
        

    pass

S = "BABBAB"

print(solution(S))
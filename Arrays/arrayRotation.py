
def solution(A, K):
    A = A[len(A) - K:len(A)] + A[0:len(A) - K]
    print(A)
    return A


solution([1, 2, 3, 4], 6)

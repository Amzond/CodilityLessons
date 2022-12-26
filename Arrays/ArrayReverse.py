


def reverse1(A):
    N = len(A)
    for i in range(N // 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    print(A)


B = [1,2,3,4]
A = [1,2,3,4]


print(B[::-1])
B.reverse()
print(B)

reverse1(A)
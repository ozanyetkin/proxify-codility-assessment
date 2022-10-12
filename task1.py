def solution(A):
    ans = 0
    for i in range(len(A)):
        if A[i] < ans:
            ans = A[i]
    return ans

N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]

dpInc = [1] * (N + 1)
dpDec = [1] * (N + 1)

maxNum = 0
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dpInc[i] = max(dpInc[i], dpInc[j] + 1)
        if reverse_A[i] > reverse_A[j]:
            dpDec[i] = max(dpDec[i], dpDec[j] + 1)
result = [0 for i in range(N)]
for i in range(N):
    result[i] = dpInc[i] + dpDec[N - i - 1] - 1

print(max(result))

N = int(input())
A = list(map(int, input().split()))
dp = [1] * (N + 1)

# 이미 dp 첫번째 인덱스는 1로 고정되어 있으므로, 첫번째 인덱스부터 검사하는 것이 맞다.
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

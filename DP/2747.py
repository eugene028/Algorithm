N = int(input())
dp = [-1] * (N + 1)
dp[0] = 0
dp[1] = 1


def fibo(a):
    if dp[a] == -1:
        dp[a] = dp[a - 2] + dp[a - 1]
    return dp[a]


for i in range(N + 1):
    dp[i] = fibo(i)
print(dp[N])

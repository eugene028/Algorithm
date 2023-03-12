T = int(input())
dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for _ in range(T):
    N = int(input())
    N = N - 1
    if N <= 4:
        print(dp[N])
    elif N > 4:
        for i in range(5, N + 1):
            dp[i] = dp[i - 1] + dp[i - 5]
        print(dp[N])

T = int(input())

dp = []

for _ in range(T):
    sticker = []
    N = int(input())
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    if len(sticker[0]) == 1:
        dp.append(max(sticker[0][0], sticker[1][0]))
    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        for i in range(2, N):
            sticker[0][i] += max(sticker[1][i - 1], sticker[1][i - 2])
            sticker[1][i] += max(sticker[0][i - 1], sticker[0][i - 2])
        dp.append(max(sticker[0][N - 1], sticker[1][N - 1]))

for j in range(len(dp)):
    print(dp[j])



N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

pre =[[0] * (N + 1) for _ in range(N + 1)]
# (i,j) 까지의 구간 합 먼저 구해보자.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        pre[i][j] = pre[i][j-1] + pre[i-1][j] - pre[i-1][j-1] + graph[i-1][j-1]
# print(pre)

max_profit = pre[0][0]
for k in range(N):
    for i in range(1, N - k + 1):
        for j in range(1, N - k + 1):
            profit = pre[i+k][j+k] - pre[i-1][j+k] - pre[i+k][j-1] + pre[i-1][j-1]
            max_profit = max(max_profit, profit)


print(max_profit)
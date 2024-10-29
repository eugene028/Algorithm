import math
from collections import deque
N, K = map(int, input().split(" "))
value = set()

dp = [math.inf for _ in range(K + 1)]
for _ in range(N):
    value.add(int(input()))

# 더하는 거밖에 없으니까 K까지 검사하면 됨.
# 1 + 1
# 5 + 5
#
# BFS를 위한 큐
queue = deque()

# 각 코인 값에 대해 dp를 초기화
for coin in value:
    if coin <= K:
        dp[coin] = 1
        queue.append(coin)
# print(dp)

while queue:
    v = queue.popleft()
    for num in value:
        nxt = v + num
        if nxt > K:
            continue
        if dp[nxt] > dp[v] + 1:
            dp[nxt] = dp[v] + 1
            queue.append(nxt)


if dp[K] == math.inf:
    print(-1)
else:
    print(dp[K])

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [0] * (N + 1)
visited = [0] * (N + 1)

#단방향 도로
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

city = []
Q = deque([X])
visited[X] = 1
dist[X] = 0

while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1
            dist[nx] = dist[c] + 1
            if dist[nx] == K:
                city.append(nx)
if len(city) == 0:
    print(-1)
else:
    city.sort()
    for result in city:
        print(result)





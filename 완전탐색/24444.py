from collections import deque
import sys

input = sys.stdin.readline
N, M, R = map(int, input().split(" "))

graph = [[] for _ in range(N + 1)]
for _ in range(M):  # 수정된 부분
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)

answer = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[R] = 1

for gp in graph:
    gp.sort()
def bfs(start):
    queue = deque([start])
    order = 1
    while queue:
        current = queue.popleft()
        answer[current] = order
        order += 1
        for i in graph[current]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

bfs(R)

for i in range(1, N + 1):
    sys.stdout.write(str(answer[i]) + '\n')
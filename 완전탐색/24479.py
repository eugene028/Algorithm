import sys
sys.setrecursionlimit(150000)

def dfs(t):
    global cnt
    visited[t] = cnt
    graph[t].sort()
    for i in graph[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트를 오름차순으로 정렬
for edges in graph:
    edges.sort()

visited = [0] * (N + 1)
stack = [R]
cnt = 1

dfs(R)

# 결과 출력
for i in range(1, N + 1):
    print(visited[i])

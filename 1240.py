from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split(" "))
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, dist = map(int, input().split(" "))
    tree[a].append((b, dist))
    tree[b].append((a, dist))

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        nd, dst = queue.popleft()
        if nd == end:
            return dst
        for n, d in tree[nd]:
            if not visited[n]:
                visited[n] = True
                queue.append((n, dst + d))

for _ in range(M):
    start, end = map(int, input().split(" "))
    print(bfs(start, end))



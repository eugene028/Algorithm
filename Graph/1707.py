import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def bfs(start):
    queue = deque([start])
    if visited[start] == 0:
        visited[start] = 1
    while queue:
        v = queue.popleft()
        color = visited[v]
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                if color == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visited[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True

for _ in range(T):
    check = 0
    V, E = map(int, input().split())
    global visited
    visited = [0] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, V + 1): #비연결 그래프인 점 고려. 모든 노드 탐색
        if not bfs(i):
            check = 1
            break
    if check == 0:
        print("YES")
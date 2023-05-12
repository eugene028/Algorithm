from collections import deque
N = int(input())
graph = []
answer = 0
xt = [1, 0, -1 ,0]
yt = [0, 1, 0, -1]
side = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

global count
count = 2
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = count
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
def bfs(n):
    global answer
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == n: #만약 있는 곳이 섬이라면
                queue.append((i, j)) #섬의 위치 저장
                visited[i][j] = -1 #방문처리
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + xt[i]
            ny = y + yt[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] > 0 and  graph[nx][ny] != n:
                answer = min(answer, visited[x][y])
            if graph[nx][ny] == 0 and visited[x][y] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            count = count + 1
for i in range(2, count):
    bfs(i)
print(answer)
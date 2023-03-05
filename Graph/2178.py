from collections import deque
Q = deque()
arr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, M = map(int, input().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

Q.append([0,0])
maze[0][0] = 1
while(len(Q) > 0):
    poped = Q.popleft()
    x = poped[0]
    y = poped[1]
    for i in range(4):
        nx = x + arr[i][0]
        ny = y + arr[i][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            Q.append([nx, ny])

print(maze[N-1][M-1])
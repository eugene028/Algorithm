from collections import deque
Q = deque()
M, N, H = map(int,input().split())
arr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
tomato = [[] for i in range(H)]
day = 0
for a in range(H):
    for _ in range(N):
        tomato[a].append(list(map(int,input().split())))

for i in range(H):
    for j in range(N):
        for z in range(M):
            if tomato[i][j][z] == 1:
                Q.append([i, j, z])

while (len(Q) > 0):
    poped = Q.popleft()
    z = poped[0]
    y = poped[1]
    x = poped[2]
    for i in range(6):
        Z = z + arr[i][0]
        Y = y + arr[i][1]
        X = x + arr[i][2]

        if X < 0 or Y < 0 or X >= M or Y >= N or Z < 0 or Z >= H:
            continue
        if tomato[Z][Y][X] == 0:
            tomato[Z][Y][X] = tomato[z][y][x] + 1
            Q.append([Z, Y, X])

for i in range(H):
    for j in range(N):
        for z in range(M):
            day = max(day, tomato[i][j][z])
            if tomato[i][j][z] == 0:
                print(-1)
                exit()
print(day - 1)
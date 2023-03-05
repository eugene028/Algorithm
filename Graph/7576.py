from collections import deque
M, N = map(int, input().split())
Q = deque()
tomato = []
day = 0
arr = [[0 , 1], [0, -1], [1, 0], [-1, 0]]
for _ in range(N):
    tomato.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append([i, j])

while (len(Q) > 0):
    poped = Q.popleft()
    x = poped[0]
    y = poped[1]
    for i in range(4):
        xn = x + arr[i][0]
        yn = y + arr[i][1]
        if xn < 0 or xn >= N or yn < 0 or yn >= M:
            continue
        if tomato[xn][yn] == 0:
            tomato[xn][yn] = tomato[x][y] + 1
            Q.append([xn, yn])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        else:
            day = max(day, tomato[i][j])

print(day - 1)

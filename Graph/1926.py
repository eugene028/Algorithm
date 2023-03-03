from collections import deque

N, M = map(int, input().split())
xd = [-1, 0, 1, 0]
yd = [0, -1, 0, 1]
pic = []
biggest = []
ans = 0
for _ in range(N):
    pic.append(list(map(int, input().split())))

def bfs(x,y):
    Q = deque()
    Q.append([x,y])
    pic[x][y] = 2 # 방문체크를 해준다.
    count = 1 # 현재 그림의 넓이를 체크합니다.
    while(len(Q)):
        poped = Q.popleft()
        x = poped[0]
        y = poped[1]
        for i in range(4):
            nx = x + xd[i]
            ny = y + yd[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if pic[nx][ny] == 1:
                pic[nx][ny] = 2
                count = count + 1
                Q.append([nx, ny])
    biggest.append(count)

for i in range(N):
    for j in range(M):
        if pic[i][j] == 1:
            bfs(i, j)
            ans = ans + 1
        j = j + 1
    i = i + 1

if ans == 0:
    print(0)
    print(0)
else:
    biggest.sort()
    print(ans)
    print(biggest[-1])




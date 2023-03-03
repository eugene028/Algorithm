from collections import deque
N = int(input())
arr = [[0 , 1], [0, -1], [1, 0], [-1, 0]]
house = []
result = []

for i in range(N):
    house.append(list(map(int, input())))
Q = deque()
def bfs(i, j):
    Q.append([i, j])
    house[i][j] = 0
    count = 1
    while(len(Q) > 0):
        poped = Q.popleft()
        x = poped[0]
        y = poped[1]
        for z in range(4):
            xn = x + arr[z][0]
            yn = y + arr[z][1]
            if xn < 0 or xn >= N or yn < 0 or yn >= N:
                continue
            if house[xn][yn] == 1:
                Q.append([xn, yn])
                count = count + 1
                house[xn][yn] = 0
    result.append(count)

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            bfs(i, j)

result.sort()
print(len(result))
for ans in result:
    print(ans)
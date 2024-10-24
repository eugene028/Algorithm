N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
answer_list = []

flattened = [item for row in arr for item in row]
max_value = max(flattened)
min_value = min(flattened)

direction = [[0,-1], [-1,0],[0,1],[1,0]]
def dfs(i,j, rain):
    visited[i][j] = 1
    stack = [(i,j)]
    while stack:
        x,y = stack.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > rain and visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))

for num in range(0, max_value + 1):
    visited = [[-1] * N for _ in range(N)]
    rain = num
    answer = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and visited[i][j] == -1:
                dfs(i, j, rain)
                answer += 1
    answer_list.append(answer)

max_value = max(answer_list)
if max_value == 0:
    print(1)
else:
    print(max_value)
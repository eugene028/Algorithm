import sys
sys.setrecursionlimit(111111)

puzzle = []
for _ in range(3):
    puzzle.append(list(map(int, input().split())))

answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
arr =  [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = []

def checkanswer():
    for i in range(3):
        for j in range(3):
            if answer[i][j] != puzzle[i][j]:
                return False

def dfs(i, j):
    global visited
    print ("i : " + str(i) + " j : " + str(j))
    if i == 2 and j == 2:
        if checkanswer():
            print("정답")
        else:
            return False

    if puzzle[i][j] == 0:
        for z in range(4):
            nx = i + arr[z][0]
            ny = j + arr[z][1]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            if [nx, ny] not in visited:
                puzzle[i][j] = puzzle[nx][ny] #바꿔치기
                puzzle[nx][ny] = 0
                visited.append([i, j])
                dfs(nx, ny)
                puzzle[nx][ny] = puzzle[i][j]
                puzzle[i][j] = 0

for i in range(3):
    for j in range(3):
        if puzzle[i][j] == 0:
            dfs(i,j)

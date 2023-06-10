#1. 가장 작은 패턴은 '3'의 패턴
# 3의 패턴으로 나누어 떨어지면 리턴과 출력을 진행합니다.

#별을 출력하는 패턴부터 익혀볼까요?

N = int(input())
answer = [[0 for _ in range(N)] for _ in range(N)]

def print3(x, y):
    for i in range(3):
        for j in range(3):
            answer[x + i][y + j] = '*'
    return

def dfs(x, y , n):
    if n == 3:
        print3(x, y)
        return
    for i in range(3):
        for j in range(3):
            dfs(x + i * (n//3), y + j * (n//3), n//3)
dfs(0,0,27)
for i in range(N):
    for j in range(N):
        print(answer[i][j], end='')
    print()
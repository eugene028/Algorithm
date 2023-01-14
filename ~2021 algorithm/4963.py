import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
def dfs(a,b):
    if(island[a][b] == 1):
        island[a][b] = 0
        for i in range(8):
            na = a + dx[i]
            nb = b + dy[i]
            if na < 0 or na >= h or nb < 0 or nb >= w:
                continue
            if island[na][nb] == 0:
                continue
            if island[na][nb] == 1:
                dfs(na,nb)
        return True
    else:
        return False

while(True):
    w,h=map(int, input().split())
    if(w==0) and (h==0): # 0 0 받으면 루프 종료합니다.
        break
    cnt = 0
    island = []  # island초기화
    for i in range(h):
        island.append(list(map(int,input().split()))) #배열 입력받기
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                cnt +=1
    print(cnt)





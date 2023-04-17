import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

n = int(input())
m = int(input())

dist = [[INT_MAX for j in range(0, 101)] for i in range(0,  101)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c
for k in range(1, n + 1): #경유지
    for i in range(1, n + 1): # 출발지
        for j in range(1, n + 1): #도착지
            if dist[i][k] != INT_MAX and dist[k][j] != INT_MAX:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or dist[i][j] == INT_MAX:
            print(0, end =' ')
        else:
            print(dist[i][j], end =' ')
    print()

import sys
import heapq
input = sys.stdin.readline
MAXINT = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(501)]
dist = [MAXINT] * (501)

def BellmanFord(K):
    negativeNum = 0
    dist[K] = 0
    for iter in range(1, N + 1):
        for cur in range(1, N + 1):
            if dist[cur] == MAXINT:
                continue
            for i in graph[cur]:
                next = i[0]
                next_dist = i[1]
                if dist[next] > dist[cur] + next_dist:
                    dist[next] = dist[cur] + next_dist
                    if iter == N :
                        negativeNum = 1
                        return negativeNum
    return negativeNum


for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
negative_cycle = BellmanFord(1)
if negative_cycle == 1:
    print(-1)
else:
    for i in range(2, N + 1):
        if(dist[i] == MAXINT):
            print(-1)
        else:
            print(dist[i])


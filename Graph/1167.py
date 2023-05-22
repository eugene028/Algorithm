from collections import deque
V = int(input())
inputlist = []
maxnum = 0
dist = [0] * (V + 1)
adj = [[] for _ in range(V + 1)] #간선 정보 담을 곳
for _ in range(V):
    inputlist = list(map(int, input().split()))
    for i in range(1, len(inputlist) - 1, 2):
        adj[inputlist[0]].append([inputlist[i], inputlist[i + 1]])
def BFS(k):
    dist = [0] * (V + 1) #초기화
    visited = [False] * (V + 1)
    dist[k] = 0 #출발자 0으로 지정
    queue = deque([[k, 0]]) #현재 노드 넣기

    while queue: #큐가 빌 때까지 넣기
        cur, cur_dist = queue.pop()
        visited[cur] = True
        for next, next_dist in adj[cur]:
            if visited[next] == True:
                continue
            dist[next] = cur_dist + next_dist #다음 갱신
            queue.append([next, dist[next]])
    maxlist = [dist.index(max(dist)), max(dist)]
    return maxlist

#모든 정점 돌면서 최대값 지정

maxnode, maxdist = BFS(1) #시작점 k로 지정
maxnode, maxdist = BFS(maxnode)

print(maxdist)
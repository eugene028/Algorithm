from collections import deque
N = int(input())
adj = [[] for _ in range(N + 1)]
for i in range(N - 1):
    inputlist = list(map(int, input().split()))
    adj[inputlist[0]].append([inputlist[1], inputlist[2]])
    adj[inputlist[1]].append([inputlist[0],inputlist[2]])
dist = [0] * (N + 1) #방문한 거리 노드
def BFS(k):
    dist = [0] * (N + 1)
    visited = [False] * (N + 1)
    dist[k] = 0
    queue = deque([[k, 0]]) #처음 노드 넣기
    while queue:
        cur, cur_dist = queue.pop()
        if visited[cur] == True:
            continue
        visited[cur] = True
        for next, next_dist in adj[cur]:
            if visited[next] == True:
                continue
            dist[next] = cur_dist + next_dist
            queue.append([next, dist[next]])
    maxlist = [dist.index(max(dist)), max(dist)]
    return maxlist
node, nodemax = BFS(1)
node, nodemax = BFS(node)

print(nodemax)
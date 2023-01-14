# Depth First Search
import sys
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] #1번 노드부터 방문, 하나 더 큰거
visited = [False] * (n + 1) #위와 마찬가지!

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 그래프를 인덱스와 그에 해당하는 노드들로 재 생성합니다.

for i in range(1, n+1):
    graph[i].sort()
#정렬을 수행합니다.

def dfs(n):
    print(n, end=' ') #해당 노드의 인덱스 번호 출력
    visited[n] = True #현재 노드 방문 처리한다.
    for i in graph[n]: #현재 노드와 연결된 노드 재귀방문문        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = True #방문처리
    queue = deque([n]) #queue로 선언.
    while queue:
        v = queue.popleft()
        print(v, end= ' ') #뽑은 것 출력
        for i in graph[v]: #아직 방문하지 않은 원소 큐 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v)
#visited 배열 초기화합니다.
visited = [False] * (n + 1)
print()
bfs(v)


"""from collections import deque

n,m,k= map(int, input().split())
visited = [False] * (m+1)

graph=[[] for _ in range(n+1)] #그래프 생성
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort() #분류한다. graph [1]부터 ..


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


dfs(graph,k,visited)
visited = [False] * (m+1)
print()
bfs(graph, k, visited)"""


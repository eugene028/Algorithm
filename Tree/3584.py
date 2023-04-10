import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

T = int(input())
NMAX = 10001
def checkdepth (idx, level, child):
    depth[idx] = level
    for k in child[idx]:
        checkdepth(k, level + 1, child)


for _ in range(T):
    N = int(input())
    depth = [0] * NMAX
    parent = [0] * NMAX
    child = [[] for _ in range(NMAX)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        child[a].append(b)
        parent[b] = a;
    root = 1
    for i in range(1, N + 1):
        if not parent[i]:
            root = i
            break
    checkdepth(root, 0, child) #노드들의 depth 계산
    a, b = map(int, input().split())
    while depth[a] < depth[b]:
        b = parent[b]
    while depth[a] > depth[b]:
        a = parent[a]
    while a != b:
        b = parent[b]
        a = parent[a]
    print(a)
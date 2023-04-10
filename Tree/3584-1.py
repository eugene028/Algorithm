T = int(input())
NMAX = 10001

for _ in range(T):
    N = int(input())
    visited = [False] * (N + 1)
    depth = [0] * NMAX
    parent = [0] * NMAX
    child = [[] for _ in range(NMAX)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        child[a].append(b)
        parent[b] = a
    root = 1
    for i in range(1, N + 1):
        if not parent[i]:
            root = i
            break

    a, b = map(int, input().split())
    visited[a] = True
    search = parent[a]
    while search != 0:
        visited[search] = True
        search = parent[search]
    while not visited[b]:
        b = parent[b]

    print(b)
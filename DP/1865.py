TC = int(input())
def check():
    dist = [0 for _ in range(N + 1)]
    dist[1] = 0
    for i in range(N):  # 모든 노드 방문
        for edge in graph:
            start, goal, time = edge
            new = dist[start] + time
            if dist[goal] > new:
                dist[goal] = new
                if i == N - 1:
                    return "YES"
    return "NO"

for _ in range(TC):
    N, M, W = map(int, input().split(" "))
    graph = []
    for _ in range(M):
        a, b, t = map(int, input().split())
        graph.append([a, b, t])
        graph.append([b, a, t])
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph.append([s, e, -t])
    print(check())





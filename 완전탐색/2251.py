from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        Q.append((x, y))

def bfs():
    while Q:
        x, y = Q.popleft()
        z = C - x - y # z는 C물통의 용량을 이야기한다.
        if x == 0:
            answer.append(z)
        # x -> y
        water = min(x, B - y)
        pour(x - water, y + water)

        # x -> z
        water = min(x, C - z)
        pour(x - water, y)

        # y -> x
        water = min(y, A - x)
        pour(x + water, y - water)

        # y -> z
        water = min(C - z, y)
        pour(x, y - water)

        # z -> x
        water = min(z, A - x)
        pour(x + water, y)

        # z -> y
        water = min(z, B - y)
        pour(x, y + water)


A, B, C = map(int, input().split())
Q = deque()
Q.append((0, 0))
visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True

answer = []

bfs()

answer.sort()
for i in answer:
    print(i, end =" ")
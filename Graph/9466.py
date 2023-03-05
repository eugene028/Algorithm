import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = students[x]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

T = int(input())
for _ in range(T):
    result = []
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i) #맨 처음엔 dfs(1)
    print(n - len(result))




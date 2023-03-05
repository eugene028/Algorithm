N, S = map(int,input().split())
arr = list(map(int, input().split()))
ans = 0
def dfs(x, y, n):
    global ans
    if y == n:
        print(result)
        if sum(result) == S:
            ans = ans + 1
        return sum(result)
    for i in range(x, k):
        result[y] = arr[i]
        dfs(i + 1, y + 1, n)

for n in range(1, N + 1):
    k = N
    result = [0] * N
    dfs(0,0,n)
print(ans)


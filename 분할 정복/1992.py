n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answerlst = []
def dfs(x, y, n):
    num_check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != num_check:
                print("(", end="")
                for k in range(2):
                    for l in range(2):
                        dfs(x + k * n // 2, y + l * n//2, n//2)
                print(")", end="")
                return
    print(str(num_check), end="")

dfs(0,0,n)

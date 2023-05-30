N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
result_minus = 0
result_zero = 0
result_plus = 0

def dfs(x, y, n):
    global result_plus, result_zero, result_minus

    num_check = lst[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if lst[i][j] != num_check: #숫자가 일치하지 않는다면
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n //3, y + l * n //3, n // 3)
                return
    if num_check == -1:
        result_minus += 1
    elif num_check == 0:
        result_zero += 1
    else:
        result_plus += 1
dfs(0, 0, N)
print(result_minus)
print(result_zero)
print(result_plus)

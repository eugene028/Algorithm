def solution(m, n, puddles):
    answer = 0
    route_map = [[0] * m for i in range(n)]
    route_map[0][0] = 1
    for puddle in puddles:
        i, j = puddle
        route_map[j - 1][i - 1] = -1

    for col in range(n):
        for row in range(m):
            if route_map[col][row] == -1:  # 만약 웅덩이를 만났다면
                continue
            elif col == 0:  # 만약 맨 위의 끝줄이라면
                if route_map[col][row - 1] > 0:
                    route_map[col][row] = route_map[col][row - 1]
                else:
                    continue
            elif row == 0:  # 만약 맨 왼쪽 끝줄이라면
                if route_map[col - 1][row] > 0:
                    route_map[col][row] = route_map[col - 1][row]
                else:
                    continue
            else:
                if route_map[col - 1][row] > 0 and route_map[col][row - 1] > 0:
                    route_map[col][row] = route_map[col - 1][row] + route_map[col][row - 1]
                elif route_map[col - 1][row] > 0 or route_map[col][row - 1] > 0:
                    num = max(route_map[col - 1][row], route_map[col][row - 1])
                    route_map[col][row] = num
                else:
                    continue

    return route_map[n - 1][m - 1] % 1000000007


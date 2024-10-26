from collections import deque
import math


def solution(board):
    n = len(board)
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dp = [[[math.inf] * 4 for _ in range(n)] for _ in range(n)]

    for i in range(4):
        dp[0][0][i] = 0

    queue = deque([(0, 0, -1)])

    while queue:
        x, y, prev_dir = queue.popleft()

        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                cost = 100
                if prev_dir != -1 and prev_dir != i:
                    cost += 500

                if prev_dir == -1:
                    new_cost = cost
                else:
                    new_cost = dp[x][y][prev_dir] + cost

                if new_cost < dp[nx][ny][i]:
                    dp[nx][ny][i] = new_cost
                    queue.append((nx, ny, i))

    return min(dp[n - 1][n - 1])

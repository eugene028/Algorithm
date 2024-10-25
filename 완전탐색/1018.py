M, N = map(int, input().split(" "))
from collections import deque
import math
# 다시 칠해야 하는 정사각형의 최소 개수. 완전 탐색으로 모든 엣지에서 시작하여 8 * 8으로 잘라보고, 그 중 최소였던 것을 리턴하면 된다.
# 완전 탐색을 수행하므로, DFS나 BFS를 사용할 것을 예측할 수 있다.
board = []

for _ in range(M):
    board.append(list(input()))

min_ans = math.inf
def check(row, col, color):
    ans = 0
    for i in range(8):
        queue = deque(board[row + i][col:col+8])
        for j in range(8):
            el = queue.popleft()
            if i % 2 == 0 and j % 2 == 0:
                if el != color[0]:
                    ans += 1
            if i % 2 == 0 and j % 2 == 1:
                if el != color[1]:
                    ans += 1
            if i % 2 == 1 and j % 2 == 0:
                if el != color[1]:
                    ans += 1
            if i % 2 == 1 and j % 2 == 1:
                if el != color[0]:
                    ans += 1
    return ans


for i in range(0, M - 8 + 1):
    for j in range(0, N - 8 + 1):
        min_ans = min(check(i, j,  ["B", "W"]), check(i, j,  ["W", "B"]), min_ans)

print(min_ans)



# 1. 뱀이 방향에 맞게 이동하면서, 도착한 곳에 사과가 있는지 없는지 체크한다.
# 처음 뱀의 몸 길이는 1으로 초기화한다. 또한, 뱀의 몸이 장악하고 있는 좌표를 저장해둔다.
# 뱀의 봄 길이가 2이상 되면 좌표 저장값은 배열이 될 것이다.
# 2. 사과가 있는 곳에 마주하였다면, 몸 길이 늘려주고 그동안 방문했던 것 중에 하나를 뽑아서 장악좌표에 넣는다.
# 3. 사과가 없는 곳에 마주하였다면, 장악 좌표 중 맨 나중에 들어왔던 아이 제거한다.
# 4. 맨 끝에 도달하거나, 장악 좌표를 도달하였다면 루프를 종료하고 답을 리턴한다.
from collections import deque

N = int(input())
K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    appleX, appleY = map(int, input().split(" "))
    board[appleX - 1][appleY - 1] = 1  # 사과 위치 표시

L = int(input())
dir = {}
for _ in range(L):
    X, C = input().split(" ")
    dir[int(X)] = C  # 시간을 키로 하여 방향 저장

# 뱀의 방향 설정 (오른쪽, 아래쪽, 왼쪽, 위쪽)
pivot = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # (r, c) 변화량
pivot_idx = 0
time = 0
path = deque()
snack_body = deque([(0, 0)])  # 뱀의 시작 위치 (머리)
r, c = 0, 0  # 뱀의 초기 머리 위치

while True:
    time += 1
    # 머리 위치 업데이트
    r += pivot[pivot_idx][0]
    c += pivot[pivot_idx][1]

    # 벽 충돌 체크
    if r < 0 or r >= N or c < 0 or c >= N or (r, c) in snack_body:
        break  # 게임 종료

    # 사과 체크
    if board[r][c] == 1:  # 사과가 있는 경우
        board[r][c] = 0  # 사과 먹기
    else:  # 사과가 없는 경우
        snack_body.popleft()  # 꼬리 제거

    snack_body.append((r, c))  # 머리 위치 추가

    # 방향 회전 처리
    if time in dir:
        if dir[time] == 'L':
            pivot_idx = (pivot_idx - 1) % 4  # 왼쪽 회전
        else:
            pivot_idx = (pivot_idx + 1) % 4  # 오른쪽 회전

print(time)  # 게임이 종료된 시간 출력
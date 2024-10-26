while True:
    # 3x3 틱택토 보드를 나타내는 리스트
    graph = [[] for _ in range(3)]

    value = input().strip()
    if value == "end":
        break
    else:
        # 3x3 형태로 보드에 값 입력
        for i in range(len(value)):
            graph[i // 3].append(value[i])

    # 기본적으로 invalid 상태로 설정
    flag = 1

    # "O"와 "X"의 개수를 세고 승리 여부 초기화
    O_count = 0
    X_count = 0

    for i in range(3):
        for j in range(3):
            if graph[i][j] == "O":
                O_count += 1
            elif graph[i][j] == "X":
                X_count += 1

    # 게임 종료 상태 조건 함수 정의
    def check_win(word):
        # 가로 검사
        for i in range(3):
            if graph[i][0] == graph[i][1] == graph[i][2] == word:
                return True
        # 세로 검사
        for i in range(3):
            if graph[0][i] == graph[1][i] == graph[2][i] == word:
                return True
        # 대각선 검사
        if (graph[0][0] == graph[1][1] == graph[2][2] == word) or (graph[0][2] == graph[1][1] == graph[2][0] == word):
            return True
        return False

    # X와 O의 승리 여부 확인
    X_win = check_win("X")
    O_win = check_win("O")

    # 게임 규칙 조건 체크
    # 1. O가 X보다 많으면 안 됨
    if O_count > X_count:
        flag = 1
    # 2. X가 O보다 2개 이상 많으면 안 됨
    elif X_count - O_count > 1:
        flag = 1
    # 3. X와 O가 동시에 이길 수 없음
    elif X_win and O_win:
        flag = 1
    # 4. O가 이긴 경우에는 O와 X의 개수가 같아야 함
    elif O_win and X_count != O_count:
        flag = 1
    # 5. X가 이긴 경우에는 X가 O보다 1개 더 많아야 함
    elif X_win and X_count != O_count + 1:
        flag = 1
    # 6. 승부가 나지 않은 경우(빈칸 존재), 게임이 끝났을 경우만 유효한 종료 상태
    elif not X_win and not O_win and O_count + X_count != 9:
        flag = 1
    else:
        flag = 0

    if flag == 1:
        print("invalid")
    else:
        print("valid")

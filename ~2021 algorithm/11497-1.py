T = int(input())
for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    answer = 0
    for i in range(2, N):
        answer = max(answer, abs(logs[i] - logs[i-2]))
    print(answer)
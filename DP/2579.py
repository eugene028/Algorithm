N = int(input())

arr = []

dp = [0]
for _ in range(N):
    arr.append(int(input()))
arr.insert(0, 0)

if len(arr) <= 3: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(arr))
else :
    dp.append(arr[1]) # 첫번재 칸 하드코딩
    dp.append(max(arr[1] + arr[2], arr[2])) #두번째 칸 - 연속해서 오르거나, 바로 건너뛰거나
    dp.append(max(arr[1] + arr[3], arr[2] + arr[3]))

    for i in range(4, N + 1):
        dp.append(max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]))

    print(dp[N])

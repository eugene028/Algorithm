n, k = map(int, input().split())
#최대 동전 종류 개수 100개까지 들어갈 수 있음
coin = [0 for i in range(101)]
dp = [10001 for i in range(k + 1)]
#dp값 MAX로 초기화, 단, MAX값에서 하나 더한 값으로 초기화
dp[0] = 0 #첫번째 dp는 0으로 정의

# 나머지 입력값 차례로 받음
for i in range(n):
    coin[i] = int(input())

for i in range(n): #동전이 3개면 3개까지만 검사해야죠.
    coinD = coin[i] # 현재 어떤 동전의 가치를 확인하고 있는지 j에다가 시시각각 저장합니다.
    for j in range(coinD, k + 1): #coin원부터 검사시작합니다. 이미 앞에 있던 친구들은 검사 끝났다..
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
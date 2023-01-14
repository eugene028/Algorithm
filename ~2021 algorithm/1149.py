
N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))
# 각 집에 대한 정보를 이차원 배열로 저장

#d[i]는 i번째 집까지의 최적의 색칠 비용이다.
d=[[0,0,0] for i in range(N)]

d[0] = RGB[0]

for i in range(1,N): #[i는 0번집, 1번집, 2번집 계산]
        d[i][0] = min(d[i-1][1]+ RGB[i][0], d[i-1][2] + RGB[i][0])
        d[i][1] = min(d[i-1][0]+RGB[i][1], d[i-1][2]+RGB[i][1])
        d[i][2] = min(d[i-1][1]+RGB[i][2], d[i-1][0]+RGB[i][2])

print(min(d[-1]))
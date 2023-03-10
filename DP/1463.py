import sys
N = int(sys.stdin.readline())

d = [0] * 1000001 #시간초과 조심하기 (백만까지 있다)

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i//2] + 1, d[i])
    elif i % 3 == 0:
        d[i] = min(d[i//3] + 1, d[i])

print(d[N])
n, m = map(int, input().split())
answer = []
r = 1
a = n
b = m
# 최대공약수
while n % m != 0:
    r = n % m
    n = m
    m = r
answer.append(m)

# 최소공배수
answer.append(int(a * b / answer[0]))

for j in answer:
    print(j)
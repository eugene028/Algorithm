
sosu = []
N = int(input())
a = [False, False] + [True]*(N-1)
for i in range(2, int(N ** 0.5) + 1):
    if a[i]:
        a[i*2::i] = [False]*((N-i)//i)

# 소수 배열 생성
for i in range(N+1):
    if a[i] == True:
        sosu.append(i)

answer = 0
start = 0
end = 0
while end <= len(sosu):
    temp_list = sum(sosu[start:end])
    if temp_list == N:
        answer = answer + 1
        end = end + 1
    elif temp_list < N:
        end = end + 1
    else:
        start = start + 1

print(answer)

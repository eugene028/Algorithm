N = int(input())
M = int(input())
Out = list(map(int, input().split()))



min_count = abs(100 - N)

#순열을 이런 식으로도 만들 수 있구나.
for check in range(1000001):
    check = str(check)

    for j in range(len(check)):
        if int(check[j]) in Out:
            break
        elif j == len(check) - 1:
            min_count = min(min_count, abs(int(check) - N) + len(check))

print(min_count)


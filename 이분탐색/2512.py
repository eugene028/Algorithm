N = int(input())
budgets = list(map(int, input().split(" ")))
M = int(input())

#상한선을 정하는 이분 탐색
start = 1
end = M

if sum(budgets) <= M:
    print(max(budgets))
    exit()

while start <= end:
    mid = (start + end) // 2
    total = 0
    for bd in budgets:
        if bd <= mid:
            total += bd
        else:
            total += mid
    if total > M:
        end = mid - 1
    else:
        start = mid + 1
print(start - 1)


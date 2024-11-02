N, M = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))

start = 0 #절단기
end = max(trees)

while start <= end:
    answer = 0
    mid = (start + end) // 2
    for tree in trees:
        res = tree - mid
        if res > 0:
            answer += res
    if answer >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
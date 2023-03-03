#나무의개수 N, 상근이가 필요한 나무길이 M
N, M = map(int, input().split())
trees = list(map(int, input().split()))
high = max(trees)
low = 1

while low <= high:
    treeSlice = []
    mid = (high + low)//2
    treeSliceSum = 0
    for i in trees:
        if i >= mid:
            treeSliceSum = treeSliceSum + i - mid
    if treeSliceSum >= M:
        low = mid + 1
    elif treeSliceSum < M:
        high = mid - 1
    #elif treeSliceSum == M:
    #    ans = mid
    #    break
print(high)




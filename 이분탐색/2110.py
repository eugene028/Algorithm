N, C = list(map(int, input().split()))
arr = []
answer = 0
for _ in range(N):
    arr.append(int(input()))

arr.sort() #정렬
start = 1 #최소 거리 설정
end = arr[-1] - arr[0] #가장 큰 값 - 가장 작은 값 (최대 거리)

while start <= end:
    print('시작:'+ str(start))
    print('최대간격' + str(end))
    mid = (start + end) // 2 #중간값
    cur = arr[0] #첫번째 좌표
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:
            cur = arr[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print('정답' + str(answer))


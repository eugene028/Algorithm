#최소값 구하기!
# 3월 1일부터, 11월 30일까지 매일 한 가지 이상 꽃이 피어 있어야 함.
N = int(input())
# 최소 개수를 고르는 것은...

targetStart = 301
targetEnd = 1130

ans = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split(" "))
    startday = sm * 100 + sd
    endday = em * 100 + ed
    ans.append([startday, endday])

ans.sort()
end_date = 301
count = 0

while len(ans) > 0:
    #정원의 마지막 꽃이 지는 날짜가 12월 1일 이상이 되거나, 현재 확인할 꽃의 시작 날짜가 정원의 마지막 날짜와 이어지지 않은 경우.
    if end_date >= 1201 or ans[0][0] > end_date:
        break
    temp_end = -1
    for _ in range(len(ans)):
        if ans[0][0] <= end_date:
            if temp_end <= ans[0][1]:
                temp_end = ans[0][1]
            ans.remove(ans[0])
        else:
            break
    end_date = temp_end
    count += 1

if end_date < 1201:
    print(0)
else:
    print(count)
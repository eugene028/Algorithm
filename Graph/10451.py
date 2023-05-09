T = int(input())

def check(num, start):
    visited[num] = True #방문처리
    if numlist[num] == start:
        return
    else:
        check(numlist[num], start)

for _ in range(T):
    answer = 0
    N = int(input())
    global numlist
    numlist = list((map(int, input().split())))
    numlist.insert(0, 0)
    global visited
    visited = [False] * (N + 1)
    for i in range(1, len(numlist)):
        if visited[i] == False: #방문하지 않은 것이면
            start = i #시작으로 지정하고
            check(i, start)
            answer = answer + 1
    print(answer)

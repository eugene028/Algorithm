import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = []
result = []

for i in range(N):
    li.append(list(map(int, input().split())))

for k in range(N): #행마다 돌아가면서 검사
    cnt = 0
    lst = []
    for i in range(N):
        if k == i:
            continue
        tmp = M - li[i].count(0)
    if tmp > 1:
        cnt += 1
    elif tmp == 1:
        for a in range(len(li[i])):
            if li[i][a] != 0:
                lst.append(a)
                cnt += len(lst)
                cnt -= len(list(set(lst)))
result.append(cnt)
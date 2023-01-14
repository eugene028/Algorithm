import sys
import copy
input=sys.stdin.readline
n,m=map(int, input().split())
boxlist=[0 for _ in range(n)]

for i in range(n):
    boxlist[i]=list(map(int, input().split()))

finallist=[]
for k in range(n):
    boxlist[k] = [0 for _ in range(m)]
    finalcount = 0
    tmpcount = 0
    for i in range(n):
        for j in range(m):
            if boxlist[i][j] > 0:
                tmpcount = tmpcount + 1
        if tmpcount >= 2:
            boxlist[i]=[0 for _ in range(m)]
            finalcount = finalcount + 1
        tmpcount = 0
    countlist=[]
    count=0
    for j in range(m):
        for i in range(n):
            if boxlist[i][j] >0 :
                count = count + 1
                if count >=2:
                    finalcount = finalcount + (count-1)
        count=0
    boxlist = copy.deepcopy(boxlist2)  # copy.deepcopy 함수를 사용하여 깊은 복사
    finallist.append(finalcount)
print(min(finallist))






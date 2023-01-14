import sys
input=sys.stdin.readline
n,m=map(int, input().split())
boxlist=[0 for _ in range(n)]
rowcheck=[0 for _ in range(50)]
visitcheck=[0 for _ in range(50)]

for i in range(n):
    boxlist[i]=list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if(boxlist[i][j]) :
            rowcheck[i]= rowcheck[i] + 1 # 각 행에 0이 아닌 것이 몇 개 있는지 체크

finalresult=[]
for k in range(n):
    finalcount = 0
    for i in range(n):
        if(i==k):
            continue
        elif (rowcheck[i]>1):
            finalcount = finalcount + 1
        elif (rowcheck[i]==0):
            continue
        else:
            checkpoint= False
            for j in range(m):
                if(boxlist[i][j] and (not visitcheck[j])):
                    visitcheck[j]=1
                    checkpoint = not checkpoint
                    break
            if (not checkpoint) :
                finalcount = finalcount +1
    finalresult.append(finalcount)

print(min(finalresult))






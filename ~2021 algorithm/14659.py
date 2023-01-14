import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
start=l.pop(0)
j=0
k=0
for i in l:
    if start>i:
        j=j+1
    else:
        start=i
        j=0
    k=max(k,j)
print(k)
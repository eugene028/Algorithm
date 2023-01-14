import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
count=0
num=len(l)
for j in range(num):
    if sum(l[:j+1])<m:
        continue
    elif sum(l[:j+1])==m:
        count+=1

    else:
        l.pop(l[0])
print(l)
print(count)


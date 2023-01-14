import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
list2=[]
list1=[]
list3=[]
for _ in range(n):
    g,x=map(int,input().split())
    list1.append(x)
for _ in range(max(list1)+1):
    list2.append(0)
for i in list1:
    list2[i]=list3[p]
    p=p+1
result=0
a=len(list2)
for j in range(a):
    if j<=2*k:
        result1=sum(list2[:j])
        if result1>=result:
            result=result1
    else:
        result1=sum(list2[:2*k+2])
        del list2[0]
        if result1>=result:
            result=result1
print(result)

import sys
from collections import deque
input=sys.stdin.readline
q=deque()
n,k=map(int,input().split())
list1=[]
for j in range(1,n+1):
    q.append(j)
while 1:
    if len(q)==0:
        break
    for _ in range(k-1):
        a=q.popleft()
        q.append(a)
    b=q.popleft()
    list1.append(b)
print("<",end="")
print(', '.join(map(str,list1)),end="")
print(">")
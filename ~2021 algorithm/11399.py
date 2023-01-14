
import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
l.sort()
l2=[]
for i in l:
    r=i*n
    l2.append(r)
    n=n-1
result=sum(l2)
print(result)



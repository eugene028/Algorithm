
import sys
input=sys.stdin.readline
l=int(input())
n=list(map(int,input().split()))
result=list()
for _ in range(l):
    t=list()
    for i in range(len(n)):
        if i%2 !=1:
            result.append(n[i])
            t.append(n[i])
    for temp in t:
        n.remove(temp)

for i in range(l):
    temp=list()
    p=""
    for _ in range(2**(i)):
        temp.append(result.pop())
    for _ in range(len(temp)):
        p=p+str(temp.pop())+" "
    print(p)

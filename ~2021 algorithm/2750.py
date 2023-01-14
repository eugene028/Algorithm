import sys
input=sys.stdin.readline
slist=[]
b=int(input())
for i in range(b):
    slist.append(int(input()))
slist.sort()
for j in slist:
    print(j)

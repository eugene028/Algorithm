
import sys
import heapq
input=sys.stdin.readline
default=[]
for _ in range(int(input())):
    a=int(input())
    if a==0:
        if len(default)==0:
            print(0)
        else:
            print(heapq.heappop(default)[1])
    else:
        heapq.heappush(default,(-a,a))




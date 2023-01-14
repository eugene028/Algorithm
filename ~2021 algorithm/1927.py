import sys
import heapq
input=sys.stdin.readline
list1=[]
for _ in range(int(input())):
    a=int(input())
    if a==0:
        if len(list1)==0:
            print(0)
        else:
            print(heapq.heappop(list1))
    else:
        heapq.heappush(list1,a)
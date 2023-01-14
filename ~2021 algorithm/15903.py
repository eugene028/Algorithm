import sys
input=sys.stdin.readline
import heapq
n,m=map(int,input().split())
list1=list(map(int,input().split()))
list2=[]
for x in list1:
    heapq.heappush(list2,x)
i=0
while(i<m):
    num1=heapq.heappop(list2)
    num2=heapq.heappop(list2)
    result=num1+num2
    heapq.heappush(list2,result)
    heapq.heappush(list2,result)
    i+=1
print(sum(list2))


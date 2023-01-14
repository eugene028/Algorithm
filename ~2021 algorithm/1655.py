import sys
import heapq
maax=[]
miin=[]
input=sys.stdin.readline
n=int(input())
for i in range(n):
    m=int(input())
    if len(maax)==len(miin):
        heapq.heappush(maax,(-1 * m,m))
    else:
        heapq.heappush(miin,(m,m))
    if miin and maax[0][1] > miin[0][1]:
        temp_min=heapq.heappop(miin)[1]
        temp_max=heapq.heappop(maax)[1]
        heapq.heappush(maax,(-1*temp_min,temp_min))
        heapq.heappush(miin,(temp_max,temp_max))
    print(maax[0][1])

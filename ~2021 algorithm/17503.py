import sys
import heapq
input=sys.stdin.readline
arr=[]
qqq=[]
ans=0
n,m,k=map(int,input().split())
for _ in range(k):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort(key=lambda x : x[1])
find=False
for i in range(k):
    now_fav,now_al=arr[i]
    heapq.heappush(qqq,now_fav)
    ans+=now_fav
    if len(qqq)>n:
        ans-=heapq.heappop(qqq)
    if len(qqq)==n and ans>=m:
        find=True
        print(now_al)
        break
if not find:
    print(-1)


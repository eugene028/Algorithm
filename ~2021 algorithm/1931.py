import sys
input=sys.stdin.readline
def greedy(arr):
    ans=1
    now_start, now_end = arr[0][0], arr[0][1]
    for i in range(1,n):
        next_start,next_end=arr[i][0],arr[i][1]
        if next_start>=now_end:
            now_start,now_end = next_start,next_end
            ans +=1
    return ans

n=int(input())
discuss=[]
for i in range(n):
    a,b=map(int,input().split())
    discuss.append((a,b))
discuss.sort(key=lambda x:(x[1],x[0]))
print(greedy(discuss))

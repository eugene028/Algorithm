n,k=map(int,input().split())

lan=[]
for j in range(n):
    m=int(input())
    lan.append(m)
left,right=1,max(lan)
answer=0
while left<=right:
    mid=(left+right)//2
    b=sum([(i//mid) for i in lan])
    if b>=n:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)
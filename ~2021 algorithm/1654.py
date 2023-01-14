"""
n,k=map(int,input().split())
lan=[]
for j in range(n):
    m=int(input())
    lan.append(m)

def one (num):
    a=0
    for i in range(k):
        a = a+ lan[i]//num
    return a>=n

def answer(left,right):
    ans=1
    while left<=right:
        mid = (left+right)//2
        if one(mid)==True:
            left=mid+1
            ans = max(ans,mid)
        else:
            right=mid-1
    return ans

print(answer(1,max(lan)))
"""
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
        result=mid
        left=mid+1
    else:
        right=mid-1
print(answer)
import math

def pre(num):
    k=int(math.log10(num))
    size=0
    for i in range(k):
        size = size + (i+1)*(10**(i+1)-10**i)
    size=size+(k+1)*(num - 10 ** k+1)
    return size
def answer(left,right):
    while left<right:
        mid=(left+right)//2
        if pre(mid)<k:
            left=mid+1
        else:
            right=mid
    return right
n,k=map(int,input().split())
num=answer(1,n)
size=pre(num)
if size<k:
    print(-1)
else:
    print(str(num)[len(str(num))-(size-k)-1])
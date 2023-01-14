"""
n=int(input())
card=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))
card.sort()
i=0
def answer(num):
    left=0
    right=len(card)
    while left<right:
        mid=(left+right)//2
        if card[mid]<num:
            left=mid+1
        elif card[mid]==num:
            i+1
        else:
            right=mid
    return i
alist=[]
for j in mlist:
    answer(j)
    alist.append(j)

print(alist)
"""
n=int(input())
card=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))
card.sort()
alist={}
for i in card:
    if i in alist:
        alist[i]= alist[i]+1
    else:
        alist[i]=1
print(" ".join(str(alist[j]) if j in alist else '0' for j in mlist))


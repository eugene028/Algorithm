n=int(input())
f_list=list(map(int,input().split()))
f_list.sort()
m=int(input())
s_list=list(map(int,input().split()))

def answer(num):
    left=0
    right=len(f_list)
    while left<right:
        mid=(left+right)//2
        if f_list[mid]<num:
            left=mid+1
        elif f_list[mid]==num:
            return 1
        else:
            right=mid
    return 0
for i in s_list:
    print(answer(i))
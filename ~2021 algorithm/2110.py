N,C=map(int,input().split())
x_list=[]
for _ in range(N):
    x=int(input())
    x_list.append(x)
x_list.sort()
left,right=x_list[1]-x_list[0],x_list[-1]-x_list[0]
m=0
while left<=right:
    mid=(left+right)//2
    me=x_list[0]
    st=1
    for j in range(1,N):
        if x_list[j]>=me+mid:
            st +=1
            me=x_list[j]
        if st>=C:
            answer=mid
            st=mid+1
        else:
            right=mid-1
print(answer)
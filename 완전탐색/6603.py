def lotto(x,y):
    if y==6:
        print(' '.join(map(str,result)))
        return
    for i in range(x,k):
        result[y]=num_list[i]
        lotto(i+1,y+1)
while 1:
    num_list=list(map(int,input().split()))
    if num_list==[0]:
        break
    k = num_list.pop(0)
    result=list(0 for _ in range(6))
    lotto(0,0)
    print()
T = int(input())
for _ in range(T):
    whatMax = 100000
    list1=[]
    list2=[]
    log=[]
    N=int(input())
    log= list(map(int, input().split()))
    log.sort()
    if(log[0]==log[len(log)-1]):
        print(0)
        continue
    log[2],log[len(log)-1]=log[len(log)-1],log[2]
    list2.append(abs(log[0] - log[len(log) - 1]))
    list2.append(abs(log[0] - log[1]))
    for i in range(2,len(log)-1):
        for j in range(2,len(log)):
            list1.append(abs(log[j]-log[j-1]))
        tmp=max(list1)
        if whatMax >= tmp:
            whatMax = tmp
        log[i],log[i+1] = log[i+1],log[i]
        list1=[]
    list2.append(whatMax)
    print(max(list2))




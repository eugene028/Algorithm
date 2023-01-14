n,m=map(int,input().split())
list1=[]
list2=[]
list3=[]
for x in range(0,n):
    x=input()
    list3=list(x)
    list1.append(list3)

for i in range(0,m-7):
    for j in range(0, n - 7):
        count1 = 0
        count2 = 0
        for x in range(j, j+8):
            for y in range(i, i+8):
                if(x+y)%2==0:
                    if list1[x][y]!='W':
                        count1+=1
                    if list1[x][y]!='B':
                        count2+=1
                else:
                    if list1[x][y]!='B':
                        count1+=1
                    if list1[x][y]!='W':
                        count2+=1
        list2.append(count1)
        list2.append(count2)

print(min(list2))




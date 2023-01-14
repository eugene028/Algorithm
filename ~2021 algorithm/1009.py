import sys
input=sys.stdin.readline

test=int(input())
alist=[]
blist=[]
for i in range(test):
    a,b=map(int,input().split())
    alist.append(a)
    blist.append(b)

for j in range(test):
    if(alist[j]%10==1 or alist[j]%10==5 or alist[j]%10==6):
        print(alist[j]%10)
    elif(alist[j]%10==2):
        if(blist[j]%4==1):
            print(2)
        elif(blist[j]%4==2):
            print(4)
        elif(blist[j]%4==3):
            print(8)
        elif(blist[j]%4==0):
            print(6)
    elif(alist[j]%10==3):
        if (blist[j] % 4 == 1):
            print(3)
        elif (blist[j] % 4 == 2):
            print(9)
        elif (blist[j] % 4 == 3):
            print(7)
        elif (blist[j] % 4 == 0):
            print(1)
    elif (alist[j] %10== 4):
        if (blist[j] % 2 == 1):
            print(4)
        elif (blist[j] % 2 == 0):
            print(6)
    elif(alist[j]%10==7):
        if(blist[j]%4==1):
            print(7)
        elif(blist[j]%4==2):
            print(9)
        elif(blist[j]%4==3):
            print(3)
        elif(blist[j]%4==0):
            print(1)
    elif(alist[j]%10==8):
        if(blist[j]%4==1):
            print(8)
        elif(blist[j]%4==2):
            print(4)
        elif(blist[j]%4==3):
            print(2)
        elif(blist[j]%4==0):
            print(6)
    elif(alist[j]%10==9):
        if(blist[j]%2==1):
            print(9)
        elif(blist[j]%2==0):
            print(1)
    elif(alist[j]%10==0): #alist[j]%10==0으로 만드니까 바로 맞았다!
        print(10)




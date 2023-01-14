import sys
input=sys.stdin.readline
n,m=map(int,input().split())
k=4
if n<=1:
    print(1)
elif n<=2:
    if k<(m+1)//2:
        print(k)
    else:
        print((m+1)//2)
else:
    if m<=6:
        if k<m:
            print(k)
        else:
            print(m)
    else:
        print(m-2)

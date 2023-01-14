import sys
input=sys.stdin.readline

NMAX=100000
l=[0 for _ in range(NMAX+1)]

n=int(input())
for _ in range(1,n):
    a, b= map(int,input().split())
    l[a] +=1
    l[b]+=1

n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    if a==2:
        print('yes')
    elif a==1:
        if l[b]>=2:
            print('yes')
        else:
            print('no')

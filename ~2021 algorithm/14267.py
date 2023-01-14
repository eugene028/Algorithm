import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
NMAX=100000
child=[[] for _ in range(NMAX + 1)]
goodjob=[0 for _ in range(NMAX + 1)]

def preorder(idx):
    for k in child[idx]:
        goodjob[k] += goodjob[idx]
        preorder(k)

n,m=map(int,input().split())
a=list(map(int,input().split()))

for i in range(1,n+1):
    if a[i-1] != -1:
        child[a[i-1]].append(i)
for _ in range(m):
    a,b=map(int,input().split())
    goodjob[a] += b

preorder(1)

for i in range(1,n+1):
    print(goodjob[i],end=' ')
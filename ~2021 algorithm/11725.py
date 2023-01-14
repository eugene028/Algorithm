import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**8)
NMAX=100000
child=[[]for _ in range(NMAX+1)]
parent=[0 for _ in range(NMAX+1)]

def order(idx):
    for k in child[idx]:
        if parent[k]==0:
            parent[k]=idx
            order(k)

n=int(input())
for _ in range(1,n):
    a,b=map(int,input().split())
    child[a].append(b)
    child[b].append(a)

order(1)

for i in range(2,n+1):
    print(parent[i])
import sys
input=sys.stdin.readline

NMAX=123456
sys.setrecursionlimit(10**8)
num=[0 for _ in range(NMAX+1)]
child=[[] for _ in range(NMAX+1)]

def postorder(idx):
    if child[idx]:
        for k in child[idx]:
            num[idx]= num[idx]+postorder(k)
        return max(num[idx],0)
    else:
        return max(num[idx],0)
n=int(input())
for i in range(2,n+1):
    a,b,c=input().split()
    num[i]=int(b)
    if a == 'W':
        num[i]= num[i]* -1
    child[int(c)].append(i)
print(postorder(1))
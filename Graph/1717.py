import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
par = [0] * 10000001
height = [1] * 1000001

for i in range(n + 1):
    par[i] = i
def findUnion(num):
    if num == par[num]:
        return num
    par[num] = findUnion(par[num])
    return par[num]

def unite(a, b):
    a = findUnion(a)
    b = findUnion(b)
    if a == b:
        return
    if height[a] < height[b]:
        a, b = b, a
    par[b] = a
    if height[a] == height[b]:
        height[a] = height[a] + 1

for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().split())
    if k == 0:
        unite(a, b)
    else:
        if findUnion(a) == findUnion(b):
            print('YES')
        else:
            print('NO')
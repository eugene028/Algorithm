import sys
N = int(sys.stdin.readline())
m = int(sys.stdin.readline())
par = [0] * (N + 1)
v = [0] * m
answer = 0

for i in range(m):
    a, b, c = map(int, input().split())
    v[i] = [c,b,a]
v.sort()
for i in range(N + 1):
    par[i] = i

def findz(num):
    if num == par[num]:
        return num
    par[num] = findz(par[num])
    return par[num]
def unite(cost, a, b):
    global answer
    a = findz(a)
    b = findz(b)
    if a == b:
        return
    par[b] = a
    answer = answer + cost

for k in v:
    unite(k[0], k[1], k[2])

print(answer)

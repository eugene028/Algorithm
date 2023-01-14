"""
a, b = map(int, input().split())
for _ in range(a):
    m = input().split()
list1 = []
list2 = []

for _ in range(a):
    list1.append(int(m[0]))
for _ in range(b):
    list2.append(int(m[1]))
n=1
for k in range(1, a):
    if list1[k - 1] != list1[k]:
        n= n + 1
    elif list1[k - 1] == list1[k]:
        if list2[k - 1] >= list2[k]:
            continue
        else:
            n= n + 1
print(n)
"""
m=0
stack=[[] for _ in range(6)]
n,p=map(int,input().split())
for _ in range(n):
    a,b=map(int,input().split())
    a=a-1
    if len(stack[a])==0:
        stack[a].append(b)
        m=m+1
    else:
        while stack[a][-1]>b:
            stack[a].pop()
            m=m+1
            if len(stack[a])==0:
                break
        if len(stack[a])==0:
            stack[a].append(b)
            m=m+1
        elif stack[a][-1]!=b:
            stack[a].append(b)
            m=m+1
print(m)
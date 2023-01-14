import sys
n=int(sys.stdin.readline())
list1=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        list1.pop()
    else:
        list1.append(a)
if len(list1)>0:
    print(sum(list1))
else:
    print(0)

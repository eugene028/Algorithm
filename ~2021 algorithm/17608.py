import sys
n=int(sys.stdin.readline())
list1=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    list1.append(a)
top=list1.pop()
list2=[top]
for j in range(1,len(list1)+1):
    if list1[-1]>top:
        list2.append(list1[-1])
        top=list1.pop()
    else:
        list1.pop()
print(len(list2))



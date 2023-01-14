"""
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
list1=[]
list2=[]
list3=[]
list4=[]
for _ in range(a+b):
    person1=input()
    person1=person1.rstrip()
    list1.append(person1)
list2=list1[0:a]
list3=list1[a+1:]
for j in list2:
    if j in list3:
        list4.append(j)
print(len(list4))
for k in sorted(list4):
    print(k)
"""
##집합의 연합의 연산
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
list1=[]
list2=[]
list1=[input() for _ in range(a)]
list2=[input() for _ in range(b)]
list3=list(set(list1)&set(list2))
list4=[x.replace("\n",'') for x in list3]
print(len(list4))
for k in sorted(list4):
    print(k)





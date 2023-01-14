"""
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
list1=[input() for _ in range(a)]

for _ in range(b):
    question=input()
    try :
        k=list1.index(question)
        print(k+1)
    except:
        num=int(question)
        k=list1[num-1]
        k.replace("\n",'')
        print(k)
"""
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
list1=[]
dicdic={}
for i in range(a):
    name=input().rstrip()
    list1.append(name)
    dicdic[name]=i+1
for _ in range(b):
    question=input().rstrip()
    try:
        print(list1[int(question)-1])
    except:
        print(dicdic[question])


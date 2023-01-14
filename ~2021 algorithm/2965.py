import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
i=0
tmp=0
num1 = b - a - 1
num2 = c - b - 1
while((num1>0) or (num2>0)):
    if (num1 >= num2):
        tmp=b
        c=tmp
        b = c - 1
    elif (num1 < num2):
        tmp=b
        a=tmp
        b=c-1
    i+=1
    num1 = b - a - 1
    num2 = c - b - 1
print(i)



num=int(input())

def calculation1(a,b):
    num1 = b
    num2 = b - 1
    if (a==1):
        return b
    for x in range(0,a-1):
        num1 = num1 * num2
        num2 = num2-1
    return num1

list1=[]
list2=[]
for x in range(0,num):
    n,k=map(int,input().split())
    list1.append(n)
    list2.append(k)
i=0
for x in range(0,num):
    number1=calculation1(list1[i],list2[i])
    number2=calculation1(list1[i],list1[i])
    print(int(number1/number2))
    i=i+1




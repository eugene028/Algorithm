import sys
input=sys.stdin.readline
num=int(input())
list1=[]
one=num//5
for i in range(1,one+1):
    two=num-(5*i)
    if two%3==0:
        three=two//3
        result=i+three
        list1.append(result)
    else:
        if num%3==0:
            list1.append(5001)
        else:
            list1.append(-1)
five=num//3
if num%3==0:
    list1.append(five)
else:
    list1.append(-1)
list2=[]
for i in list1:
    if i>0:
        list2.append(i)
    else:
        continue
if len(list2)>0:
    print(min(list2))
else:
    print(-1)



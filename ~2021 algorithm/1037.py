num=int(input())
x=input()
list1=x.split(" ")
list1=map(int,list1)
list1=list(list1)

min_num=min(list1)
max_num=max(list1)

result=min_num*max_num
print(result)
    
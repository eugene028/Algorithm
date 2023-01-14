n=int(input())
n_list=[]
for i in range(n):
    n_list.append(list(map(int,input().split())))
n_list.sort(key=lambda x:(x[0],x[1]))
for j in n_list:
    print(j[0],j[1])
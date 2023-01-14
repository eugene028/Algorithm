n=int(input())
n_list=[]
for i in range(n):
    n,k,e,m=input().split()
    n_list.append((n,int(k),int(e),int(m)))
n_list.sort(key=lambda x : (-x[1], x[2],-x[3],x[0]))
for i in n_list:
    print(i[0])
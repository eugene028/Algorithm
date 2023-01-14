def mm(x,y,z):
    if z==">":
        return x>y
    if z=="<":
        return x<y
    return True

def ag(a,b):
    global minm,maxm
    if a == k+1:
        if int(b)<int(minm):
            minm=b
        if int(b)>int(maxm):
            maxm=b
        return
    for i in range(10):
        if result[i]==False:
            if a==0 or mm(int(b[a-1]),i,arr[a-1])==True:
                result[i]=True
                ag(a+1,b+str(i))
                result[i]=False
result=list(False for _ in range(10))
k=int(input())
arr=list(map(str,input().split()))
minm="100000000000"
maxm="0"
ag(0,'')
print(maxm)
print(minm)




import sys

def greedy(arr):
    global money
    ans=0
    for i in range(n):
        if money<0:
            break
        temp=money//arr[i]
        ans +=temp
        money-=(temp *arr[i])
    return ans
n,money=map(int,sys.stdin.readline().split())
coin=[]
for i in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)
print(greedy(coin))
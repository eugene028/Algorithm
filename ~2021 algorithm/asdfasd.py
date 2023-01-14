result=[]
def plus():
    global ans
    ans = [1, 2, 4]
    if num==1:
        return 1
    if num==2:
        return 2
    if num==3:
        return 3
    else:
        for i in range(num - 3):
            sum1 = sum(ans[-3:])
            ans.append(sum1)
            result.append(sum1)
num = int(input())

for i in range(num):
    answer = plus(int(input()))






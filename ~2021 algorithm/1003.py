N = int(input())
zero = [1,0,1] #초기배열 세팅
one = [0,1,1] #초기배열 세팅

def fibonacci(n) :
    if len(zero) <= n : #초기배열 세팅보다 큰 값일 때, 새롭게 계산하기 위함!
        for i in range(len(zero), n+1) :
            zero.append(zero[i-1]+zero[i-2]) #작은 값들 하나씩 쌓아가기.
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(N) :
    num = int(input())
    fibonacci(num)
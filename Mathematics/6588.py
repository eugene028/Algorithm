
array= [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False
#소수들만 쫙 뽑아냄 !
while(True):
    n = int(stdin.readline())

    for i in range(3, len(array)):
        if array[i] and array[n - i]:
            print(n, "=", i, "+", n - i)
            break
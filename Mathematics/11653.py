import math
result = []
N = int(input())
array = [True] * (N + 1)
for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        for j in range(i + i, N+1 , i):
            array[j] = False

prime = [i for i in range(2, N + 1) if array[i] == True]
i = 0
if N == 1:
    exit()
while(N != 1):
    if N % prime[i] == 0:
        result.append(prime[i])
        N = N // prime[i]
    else:
        i = i + 1

for i in result:
    print(i)

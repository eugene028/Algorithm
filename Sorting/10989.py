import sys
N = int(input())

arr = [0] * 100001
for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] = arr[num] + 1

for i in range(1, 100001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
N = int(input())
num = 1
if N == 0:
    print(1)
    exit()
for i in range(1, N + 1):
    num = num * i
print(num)
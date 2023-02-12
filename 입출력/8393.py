import sys
n = int(sys.stdin.readline().rstrip())

num = 0
for i in range(1, n + 1):
    num = num + i
    i = i + 1
print(num)
import sys
N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print("*" * i + " " * (N - i), end='')
    print(" " * (N - i) + "*" * i)

for i in range(1, N):
    print("*" * (N - i) + " " * i, end='')
    print(" " * i + "*" * (N - i))

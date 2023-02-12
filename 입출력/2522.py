import sys
N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)

for i in range(1, N):
    print(" " * i + "*" * (N - i))
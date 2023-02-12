import sys
N = int(sys.stdin.readline())

for i in range(1, N):
    print(" " * (N - i - 1), end ='')
    for j in range(i):
        print(" ", end='')
        print("*", end ='')
    print("")

print("*" * ( 2 * N - 1))
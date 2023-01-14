import sys
input=sys.stdin.readline
num=int(input())

for i in range(num):
    k = 2 * i + 1
    for a in range(num-(i+1)):
        print(' ',end='')
    for j in range(k):
        print('*',end='')
    print()


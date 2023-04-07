import sys

N = int(input())
A = 1
res =''
if not N:
    sys.stdout.write('0')
    exit()
while( N != 0 ):
    if N % -2 < 0:
        A = N // -2
        N = A + 1
        res = res + str(1)
    else:
        N = N // -2
        res = res + str(0)

print(res[::-1])
A, B = map(int, input().split())
r = 1
while(A % B != 0):
    r = A % B
    A = B
    B = r
print('1' * B)
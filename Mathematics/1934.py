T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    r = 1
    a , b = A, B
    while(A % B != 0):
        r = A % B
        A = B
        B = r
    max = B
    print(int(a * b / max))
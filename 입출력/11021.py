T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    num = A + B
    print("Case #%d: %d" %(i + 1, A + B))
    #print("Case #" + str((i + 1)) + ": " + str(num))
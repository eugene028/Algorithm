num = int(input())
ans = [1, 2, 4]
for i in range(3, 10):
    ans.append(sum(ans[-3:]))
for i in range(num):
    n = int(input())
    print(ans[n - 1])
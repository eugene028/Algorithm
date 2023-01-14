n, m = input("").split()
n = int(n)
m = int(m)
list_num = list(map(lambda x: int(x), list(input("").split())))
result = 0
for j in range(0, n):
    for k in range(j + 1, n):
        for z in range(k + 1, n):
            result_1 = list_num[j] + list_num[k] + list_num[z]
            if result_1 >= result and result_1 <= m:
                result = result_1
print(result)


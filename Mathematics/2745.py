system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
answer = []
result = 0
for i in N:
    answer.append(system.index(i))
b = 1
for i in range(len(N) - 1, 0, -1):
    result = result + int(answer[i]) * b
    b = b * int(B)


result = result + int(answer[0]) * b
print(result)
num = input()
system = "01234567"
answer = []
result = 0
b = 1
for i in range(len(num) - 1, 0, -1):
    result = result + int(num[i]) * b
    b = b * 2
result = result + int(num[0]) * b

while result != 0:
    answer.append(system[result % 8])
    result //= 8

answer = answer[::-1]
anwer = ''.join(s for s in answer)
print(anwer)
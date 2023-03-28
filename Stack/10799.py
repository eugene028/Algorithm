wood = list(input())
result = 0
count = [0] * 100001
lst = []
i = 0
while (i < len(wood) - 1 ):
    if wood[i] == '(' and wood[i + 1] == '(':
        lst.append(wood[i])
        i = i + 1
    elif wood[i] == '(' and wood[i + 1] == ')':
        for j in range(len(lst)):
            count[j] = count[j] + 1
        i = i + 1
    elif wood[i] == ')' and wood[i + 1] == '(':
        i = i + 1
    elif wood[i] == ')' and wood[i + 1] == ')':
        result = result + count[len(lst) - 1] + 1
        count[len(lst) - 1] = 0
        lst.pop()
        i = i + 1

print(result)
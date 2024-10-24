X = int(input())
cnt = 1
stack = [64]
while True:
    if sum(stack) == X:
        break
    st = stack.pop()
    value = st // 2
    if value + sum(stack) >= X:
        stack.append(value)
    else:
        stack.append(value)
        stack.append(value)


print(len(stack))
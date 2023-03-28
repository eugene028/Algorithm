str = input()
strlst = []
for i in str:
    strlst.append(i)
M = int(input())
indx = len(strlst)
for _ in range(M):
    a = input()
    if a[0] == 'P':
        a, b = a.split(" ")
        strlst.insert(indx, b)
        indx = indx + 1
    elif a == 'L':
        if indx == 0:
            continue
        indx = indx - 1
    elif a == 'D':
        if indx == len(strlst) - 1:
            continue
        indx = indx + 1
    elif a == 'B':
        if indx == 0:
            continue
        indx = indx - 1
        strlst.pop(indx)

result = ''.join(s for s in strlst)
print(result)






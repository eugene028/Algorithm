N = int(input())
num = 1
count = 0
strlst = ""
if N == 0:
    print(0)
    exit()
for i in range(1, N + 1):
    num = num * i
strlst = str(num)
strlst = strlst[::-1]
for x in strlst:
    if x != '0':
        break
    count = count + 1
print(count)
n = int(input())
num = list()
for i in range(n):
    num.append(int(input()))

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 12):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

for i in range(len(num)):
    print(d[num[i]])
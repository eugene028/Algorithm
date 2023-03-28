from string import ascii_lowercase
S = input()
dic = {}
for i in ascii_lowercase:
    dic[i] = -1

for i in S:
    dic[i] = S.index(i)

for value in dic.values():
    print(value, end = ' ')

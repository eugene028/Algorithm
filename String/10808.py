from string import ascii_lowercase
S = input()
dic = {}
for i in ascii_lowercase:
    dic[i] = 0

for i in S:
    dic[i] = dic[i] + 1

for value in dic.values():
    print(value, end = ' ')

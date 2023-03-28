S = input()
answer = []

for i in range(0, len(S)):
    answer.append(S[i::])
answer.sort()
for i in answer:
    print(i)



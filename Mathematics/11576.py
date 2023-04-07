A, B = map(int, input().split())
m = int(input())
answer = []
numlst = list(map(int, input().split()))
result = 0
num = 1
for i in range(len(numlst) - 1, 0, -1):
    result = result + numlst[i] * num
    num = num * A
result = result + numlst[0] * num
while(result != 0):
    answer.append(result % B)
    result = result // B

answer = answer[::-1]
final = ""
final = ' '.join(str(s) for s in answer)
print(final)


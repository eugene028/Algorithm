N, B = map(int, input().split())
answer = []
while(N != 0):
    r = N // B
    answer.append(N % B)
    N = r
for i in range(len(answer)):
    if answer[i] >= 10:
        answer[i] = chr(answer[i] + 55)
answer = answer[::-1]
result = ''.join(str(s) for s in answer)

print(result)

S = input()
answer = []
#아스키 코드 65 = A , 90 = Z // 97 = a , 122 = z
for i in range(0, len(S)):
    if ord(S[i]) >= 65 and ord(S[i]) <= 90:
        if ord(S[i]) <= 77:
            newNum = ord(S[i]) + 13
            answer.append(chr(newNum))
        else:
            plus = ord(S[i]) - 78
            newNum = 65 + plus
            answer.append(chr(newNum))
    elif ord(S[i]) >= 97 and ord(S[i]) <= 122:
        if ord(S[i])<= 109:
            newNum = ord(S[i]) + 13
            answer.append(chr(newNum))
        else:
            plus = ord(S[i]) - 110
            newNum = 97 + plus
            answer.append(chr(newNum))
    else:
        answer.append(S[i])
        continue
result = ''.join(s for s in answer)
print(result)


S=input()
cnt = 0

for i in range(len(S)-1):
    if S[i]==S[i+1]:
        continue
    else:
        cnt = cnt + 1

if cnt % 2 ==0 :
    print(cnt//2)
else:
    print((cnt+1)//2)

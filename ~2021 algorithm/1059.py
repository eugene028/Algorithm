L = int(input())
S=[]
S=sorted(map(int,input().split()))
S=[0]+S
n=int(input())
result=0


for i in range(0, len(S)):
    if (i != len(S)-1):
            if (S[i]==n):
                result=0
                break
            elif(S[i]<n<S[i+1]):
                result = (S[i+1]-n) * (n-S[i]-1) + S[i+1]-1-n
                break
    else:
        break
print(result)
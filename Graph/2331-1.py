A, P = map(int, input().split())
numlist = []

def calnum(num, P):
    a = []
    while (num != 0):
        a.append(num % 10)
        num = num // 10
    number = 0
    for i in range(len(a)):
        number = number + a[i] ** P
    return number
numlist.append(A)
i = 0
while True:
    num = numlist[i] #인덱스 뽑아서
    nextnum = calnum(num, P) #다음 인덱스값 계산
    if nextnum not in numlist:
        numlist.append(nextnum)
        i += 1
    else:
        indx = numlist.index(nextnum)
        print(indx)
        break
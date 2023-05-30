from collections import deque
N = int(input())
count = 0
answer0 = 0
answer1 = 0
answern1 = 0
lst=[]
alst=[]
for _ in range(N):
    alst = list(map(int, input().split()))
    lst.append(alst)
#print(lst)

count = N // 3

def checknum(x1, y1, x2, y2):
    global answer0
    global answer1
    global answern1
    cnt = 0
    list1 =[]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            list1.append(lst[i][j])

    num = list1[0]
    for i in range(1, 9):
        if num == list1[i]:
            cnt = cnt + 1
    if cnt == 8:
        if num == 1:
            answer1 = answer1 + 1
        elif num == -1:
            answern1 = answern1 + 1
        else:
            answer0 = answer0 + 1
    else:
        for i in range(9):
            if list1[i] == 1:
                answer1 = answer1 + 1
            elif list1[i] == -1:
                answern1 = answern1 + 1
            else:
                answer0 = answer0 + 1
#print(count)
#이차원 배열 짤라서 9개씩 반환하기
for i in range(count):
    for j in range(count):
        j = j * 3
        checknum(i * 3, j, i * 3 + 2, j + 2)
        #print("첫배열 " + str(i*3) +', ' + str(j) + ' 뒷배열 ' + str(i*3 +2),', ' + str(j + 2))

if answer1 == 0 and answer0 == 0:
    print(1) #-1
    print(0) # 0
    print(0) # 1
elif answer0 == 0 and answern1 == 0:
    print(0) #-1
    print(0) # 0
    print(1) # 1
elif answer1 == 0 and answern1 == 0:
    print(0) #-1
    print(1) # 0
    print(0) # 1
else:
    print(answern1)
    print(answer0)
    print(answer1)

    # 0,0 <=> 2,2
    # 0,3 <=> 2,5
    # 0,6 <=> 2,8
    # ====
    # 3,0 <=> 5,2
    # 3,3 <=> 5,5
    # 3,6 <=> 5,8
    # ===
    # 6,0 <=> 8,2
    # 6,3 <=> 8,5
    # 6,6 <=> 8,8

# [x1, y1] 시작 [x2, y2] 끝









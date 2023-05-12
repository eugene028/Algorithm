from collections import deque

A, P = map(int, input().split())
visited = [0] * 10000 #숫자 담을 배열

#계산하는 함수
def calnum(num, P):
    a = []
    while (num != 0):
        a.append(num % 10)
        num = num // 10
    number = 0
    for i in range(len(a)):
        number = number + a[i] ** P
    return number
start = calnum(A, P)
visited[start] = 1 #방문처리
answer = 1
def bfs(num, answer):
    lenlist = deque([num])
    while lenlist:
        x = lenlist.popleft()
        nextnum = calnum(x, P)
        if visited[nextnum] == 0:
            visited[nextnum] = 1
            lenlist.append(nextnum)
            answer += 1
        print(lenlist)
    return answer
print(bfs(start, answer) - 1)
# i = 0
# while True:
#     num = numlist[i] #인덱스 뽑아서
#     nextnum = calnum(num, P) #다음 인덱스값 계산
#     if nextnum not in numlist:
#         numlist.append(nextnum)
#         i += 1
#     else:
#         indx = numlist.index(nextnum)
#         if indx == 0:
#             print(0)
#             exit()
#         numlist = numlist[0:indx+1]
#         break


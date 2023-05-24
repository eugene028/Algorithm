import sys
 #input() 입력시간 최대한 줄임

## 파이썬은 1초에 2000만까지 계싼 가능하다.
#요소 하나씩 검사하는 풀이법은 최대 500,000 * 500,000 시간 초과 발생
N = int(sys.stdin.readline())
mycard = list(map(int, sys.stdin.readline().split()))#이미 500,000

M = int(sys.stdin.readline())
cardlist = list(map(int, sys.stdin.readline().split()))
origin=[]
for i in cardlist:
    origin.append(i)
cardlist.sort()
answer = [-1] * M #방문 노드 체크
answer_list = [0] * M
def findNum(num):
    start = 0
    end = len(cardlist) - 1
    while start <= end:
        mid = (start + end)//2
        if cardlist[mid] > num:
            end = mid - 1
        elif cardlist[mid] < num:
            start = mid + 1
        elif cardlist[mid] == num: #찾아브렀다!
            answer[mid] = 1
            return
    return # 못찾은 경우

for i in mycard:
    findNum(i)

for i in range(M):
    if answer[i] == 1:
        answer_list[origin.index(cardlist[i])] = 1


str = ' '.join(str(s) for s in answer_list)
print(str)

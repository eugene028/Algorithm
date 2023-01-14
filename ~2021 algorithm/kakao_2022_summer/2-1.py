def solution(queue1, queue2):
    count = 0
    backup1=queue1[:]
    backup2=queue2[:]
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 == 1 :
        return -1
    sol = (sum1 + sum2)/2
    if (sum(queue1)==sol): #처음부터 같은 건 count = 0
        return count
    if (sol < max(max(queue1),max(queue2))):
        return -1

    while(True):
        if(backup1 == queue1):
            return -1
        if(backup2 == queue2):
            return -1
        if(sum(queue1)== sol): #정상적인 종료조건
            return count
        if(sum(queue1) > sol): #바꾸기 과정
            queue2.append(queue1.pop(0))
            count = count + 1
        elif (sum(queue2)> sol): # 바꾸기 과정 2
            queue1.append(queue2.pop(0))
            count = count + 1

x= solution([1,2,1,2],[1,10,1,2])
print(x)
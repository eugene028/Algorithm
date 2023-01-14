
def solution(queue1, queue2):
    count = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 == 1 : #두 수의 합이 홀수일 경우 -1
        return -1
    sol = (sum1 + sum2)/2

    if (sum(queue1)==sol):
        return count

    while(True):
        if(len(queue1) == 0): #두개의 합이 1/2로 나누어지지 않을 경우
            return -1
        if (len(queue2) == 0):  # 두개의 합이 1/2로 나누어지지 않을 경우
            return -1
        if(sum(queue1)== sol):
            break
        if(sum(queue1) > sol):
            queue2.append(queue1.pop(0))
            count = count + 1
        elif (sum(queue2)> sol):
            queue1.append(queue2.pop(0))
            count = count + 1
    return count

x= solution([1,2,1,2],[1,10,1,2])
print(x)



#----
def solution(queue1, queue2):
    count = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    final_sum = sum1 + sum2
    if (final_sum) % 2 == 1:  # 두 수의 합이 홀수일 경우 -1
        return -1
    sol = (final_sum) / 2

    if (sum(queue1) == sol):
        return count

    while (True):
        if (final_sum - max(max(queue2),max(queue1)) < sol):
            return -1
        if (sum(queue1) == sol):
            break
        if (sum(queue1) > sol):
            queue2.append(queue1.pop(0))
            count = count + 1
        elif (sum(queue2) > sol):
            queue1.append(queue2.pop(0))
            count = count + 1
    return count

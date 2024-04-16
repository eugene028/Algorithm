def solution(n, s):
    answer = []
    num = s // n
    if num == 0:
        return [-1]
    for i in range(n):
        answer.append(num)
    remain_num = s - sum(answer)
    while remain_num:
        for i in range(len(answer)):
            if remain_num == 0:
                break
            answer[i] = answer[i] + 1
            remain_num = remain_num - 1
    answer.sort()
    return answer


def tiredCheck(k, dungeons, answer):
    max_answer = answer
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            max_answer = max(max_answer, tiredCheck(k - dungeons[i][1], dungeons[:i] + dungeons[i+1:], answer + 1))

    return max_answer
def solution(k, dungeons):
    answer = tiredCheck(k, dungeons, 0)
    return answer
import heapq
def solution(operations):
    answer = []
    for i in operations:
        operation, number = i.split(" ")
        if operation == 'I':
            heapq.heappush(answer, int(number))
        else:
            if len(answer) == 0:
                continue
            elif number == "-1":
                heapq.heappop(answer)
            elif number == "1":
                answer = [-x for x in answer]
                heapq.heapify(answer)
                -heapq.heappop(answer)
                answer = [ -x for x in answer]
                answer.sort()
        print(answer)
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]
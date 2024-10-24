# 내가 헷갈렸던 부분. 요청 순서대로 처리하는 것이 아니라, 가장 효율적인 방법이 있다면 순서 바꾸어서 수행해도 괜찮지 않을까? 생각했던 것.
# 기본적으로는 요청 순서대로 수행하되, 요청을 진행하다가 새로운 작업이 들어오면 그 작업을 힙에 넣고
# 힙에 넣은 작업 중 가장 작은 소요 시간을 가진 것을 수행하면 된다.

import heapq


def solution(jobs):
    jobs.sort()
    count, last = 0, -1
    wait = []
    time = jobs[0][0]  # 첫 시작 포인트
    answer = 0
    while count < len(jobs):
        for start, term in jobs:
            if last < start <= time:
                heapq.heappush(wait, [term, start])
        if len(wait) > 0:
            last = time
            new_time, new_start = heapq.heappop(wait)
            count += 1
            time += new_time
            answer += (time - new_start)
        else:
            time += 1

    return answer // len(jobs)

# 최단시간으로 오고가는 학생들의 시각 구하기 집 -> 파티장 -> 집
# dp배열을 만들어서, dp 모든 학생들 중 max값을 구하면 되지 않을까 싶다.
import math
import heapq
N, M, X = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
go_party = [math.inf for _ in range(N + 1)]
for i in range(1, M + 1):
    start, end, time = map(int,input().split(" "))
    graph[start].append([end, time])
def dijkstra(start):
    dp = [math.inf for _ in range(N + 1)]  # 다익스트라 그래프 초기화
    dp[start] = 0
    heap = [(0, start)]  # 거리 기준으로 최소 요소를 뽑아 쓸 것이기 때문에 튜플의 0번 인덱스에 값 두기

    while heap:
        dist, current = heapq.heappop(heap)
        if dp[current] < dist:
            continue  # 현재 위치가 더 작다면 갱신하지 않음
        for next_node, next_time in graph[current]:
            new_dist = dist + next_time
            if new_dist < dp[next_node]:
                dp[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    return dp

x_to_all = dijkstra(X)

max_time = 0
for i in range(1, N + 1):
    all_to_x = dijkstra(i)
    total_time = all_to_x[X] + x_to_all[i]
    max_time = max(max_time, total_time)

print(max_time)
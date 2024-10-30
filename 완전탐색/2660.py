from collections import deque
person = int(input())

# 서로 노드 관계에 있는 것은, 더 작은 숫자 쪽을 부모 노드로 삼아서 모이면 된다.
friendList = [[] for _ in range(person + 1)]
answer = []

while True:
    a, b = map(int, input().split(" "))
    if a == -1 and b == -1:
        break
    else:
        friendList[a].append(b)
        friendList[b].append(a)

for i in range(1, person + 1):
    count = 0
    visited = [0 for _ in range(person + 1)]
    queue = deque([(i, 0)])
    visited[i] = 1
    while len(queue) > 0:
        current, dist = queue.popleft()
        count = max(count, dist)
        for j in friendList[current]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append((j, dist+1))
    answer.append([i, count])

answer.sort(key=lambda x : x[1])
min_score = answer[0][1]

true_answer = []
for ans in answer:
    if ans[1] == min_score:
       true_answer.append(ans[0])
print(f"{min_score} {len(true_answer)}")
true_answer.sort()
ans_str = " ".join(map(str,true_answer))
print(ans_str)
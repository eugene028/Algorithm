import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

union_list = [a for a in range(n+1)]
answer = []
#1은 1번째 집합에 존재함.

def union_set(a, b):
    parent_nodeA = find(a)
    parent_nodeB = find(b)
    if (parent_nodeA != parent_nodeB):
        union_list[parent_nodeB] = parent_nodeA
def find(value):
    #만약 자기 자신과 값이 같다면 대표 노드 반환
    if union_list[value] == value:
        return value
    #아니라면 인덱스 찾아가기
    else:
        union_list[value] = find(union_list[value])
        return union_list[value]

for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().split())
    if k == 0:
        union_set(a,b)
    if k == 1:
        if find(a) == find(b):
            answer.append('YES')
        else:
            answer.append('NO')

for ans in answer:
    print(ans)
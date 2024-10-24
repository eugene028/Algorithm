import sys
T = int(input())
limit_number = 15000
sys.setrecursionlimit(limit_number)

def find_parent(num, stack):
    parent = num
    stack.append(parent)
    for i, lst in enumerate(tree_node):
        if num in lst:
            parent = i
            break
    else:
        return stack
    return find_parent(parent, stack)


for _ in range(T):
    tree_node = [[] for _ in range(10001)]
    N = int(input())
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree_node[a].append(b)
    fa, fb = map(int, input().split())
    a_answer = []
    b_answer = []
    find_parent(fa, a_answer)
    find_parent(fb, b_answer)

    if len(a_answer) >= len(b_answer):
        for ans in a_answer:
            if ans in b_answer:
                print(ans)
                break
    else:
        for ans in b_answer:
            if ans in a_answer:
                print(ans)
                break


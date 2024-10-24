from itertools import permutations, combinations
n = int(input())
k = int(input())
arr = [input().strip() for _ in range(n)]
trueAnswer = set()
for num in combinations(arr,k):
    for answer in permutations(num,k):
        trueAnswer.add("".join(answer))

print(len(trueAnswer))
N = int(input())
numlst = list(map(int, input().split()))
answer = []
for i in range(len(numlst)):
    j = numlst[i]
    for z in range(2, j):
        if j % z == 0:
            numlst[i] = 0
            break
remove_set = {0, 1}
numlst = [i for i in numlst if i not in remove_set]

print(len(numlst))
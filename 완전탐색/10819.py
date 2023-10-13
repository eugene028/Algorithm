import sys
import itertools
N = sys.stdin.readline()
numlist = list(map(int, sys.stdin.readline().split()))
permutationList= list(itertools.permutations(numlist))
maxNum = 0
for mylist in permutationList:
    maxTemp = 0
    for j in range(0, len(mylist)-1):
        temp = abs(mylist[j] - mylist[j+1])
        maxTemp = maxTemp + temp
    if maxTemp > maxNum:
        maxNum = maxTemp
print(maxNum)
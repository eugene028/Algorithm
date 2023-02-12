import sys
N = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
print('%d %d' % (min(numlist), max(numlist)))
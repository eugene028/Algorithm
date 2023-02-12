import sys
#M, D = sys.stdin.readline().split(' ')
#M = int(M)
#D = int(D)

M, D = map(int, sys.stdin.readline().split())
daylist = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num = 0
for i in range(M):
    num = num + daylist[i]
num = num + D

num = num % 7

if num == 1:
    week = 'MON'
elif num == 2:
    week = 'TUE'
elif num == 3:
    week = 'WED'
elif num == 4:
    week = 'THU'
elif num == 5:
    week = 'FRI'
elif num == 6:
    week = 'SAT'
elif num == 0:
    week = 'SUN'

print(week)
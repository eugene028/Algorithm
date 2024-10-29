import math
X, Y = map(int, input().split())
Z = Y * 100 // X  # 현재 승률

if Z >= 100:  # 이미 100%면 더 이상 증가 불가능
    print(-1)
    exit()

# 목표 승률은 현재 승률 + 1
target = Z + 1

# (Y + a) / (X + a) * 100 = target
# 100(Y + a) = target(X + a)
# 100Y + 100a = targetX + targeta
# 100a - targeta = targetX - 100Y
# a(100 - target) = targetX - 100Y
# a = (targetX - 100Y) / (100 - target)

answer = (target * X - 100 * Y) / (100 - target)
if answer <= 0:
    print(-1)
else:
    print(math.ceil(answer))
T = int(input())
for _ in range(T):
    N = int(input())
    left, right = 1, 10 ** 9
    answer = 1

    while left <= right:
        mid = (left + right) // 2
        total = mid * (mid + 1) // 2

        if total <= N:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)
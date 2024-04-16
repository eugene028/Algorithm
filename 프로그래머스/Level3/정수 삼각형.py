def solution(triangle):
    mylist = [[] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        if i == len(triangle)-1:
            break
        for j in range(len(triangle[i])):
            number = triangle[i][j]
            if j == 0:
                triangle[i+1][j] = number + triangle[i+1][j]

            if j + 1 < len(triangle[i]):
                number2 = triangle[i][j+1]
                decision = max(number + triangle[i+ 1][j+1], number2+ triangle[i+1][j+1])
                triangle[i+1][j+1] = decision
            if j == len(triangle[i]) - 1:
                triangle[i+1][j+1] = number + triangle[i+1][j+1]

    answer = max(triangle[-1])

    return answer
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer


def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1):
        if x % i == 0:
            return False
    return True
T = int(input())

for _ in range(T):
    answer = []
    line = list(map(int, input().split()))
    n = line[0]
    del line[0]
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b = line[i], line[j]
            r = 1
            while(a % b != 0):
                r = a % b
                a = b
                b = r
            answer.append(b)
    print(sum(answer))


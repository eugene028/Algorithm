
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
def solution(k, tangerine):
    count_dict = {}
    answer = 0

    for value in tangerine:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1

    tangerineBox = []

    for value, count in count_dict.items():
        tangerineBox.append([value, count])

    tangerineBox.sort(key=lambda x: x[1], reverse=True)

    for i in range(k):
        if tangerineBox[answer][1] == 0:
            answer = answer + 1
        tangerineBox[answer][1] = tangerineBox[answer][1] - 1

    return answer + 1
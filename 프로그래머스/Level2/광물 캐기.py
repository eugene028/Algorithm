def solution(picks, minerals):
    mineralnum = []
    answer = 0
    count = 0
    num = 0
    for mineral in minerals:
        count = count + 1
        if mineral == 'diamond':
            num = num + 25
        elif mineral == 'iron':
            num = num + 5
        elif mineral == 'stone':
            num = num + 1
        if count == 5:
            mineralnum.append(num)
            num = 0
            count = 0
    mineralnum.append(num)
    dokisun = [-1 for _ in range(len(mineralnum))]
    rankingmineral = mineralnum[:]
    rankingmineral.sort(reverse=True)

    for num in rankingmineral:
        if picks[0] > 0:
            index = mineralnum.index(num)
            dokisun[index] = 1
            picks[0] = picks[0] - 1
            mineralnum[index] = 0
        elif picks[1] > 0:
            index = mineralnum.index(num)
            dokisun[index] = 2
            picks[1] = picks[1] - 1
            mineralnum[index] = 0
        elif picks[2] > 0:
            index = mineralnum.index(num)
            dokisun[index] = 3
            picks[2] = picks[2] - 1
            mineralnum[index] = 0
    count = 0
    i = 0
    for mineral in minerals:
        count = count + 1
        doki = dokisun[i]
        if doki == -1:
            break
        if mineral == 'diamond':
            if doki == 1:
                answer = answer + 1
            elif doki == 2:
                answer = answer + 5
            elif doki == 3:
                answer = answer + 25
        elif mineral == 'iron':
            if doki == 1:
                answer = answer + 1
            elif doki == 2:
                answer = answer + 1
            elif doki == 3:
                answer = answer + 5
        elif mineral == 'stone':
            if doki == 1:
                answer = answer + 1
            elif doki == 2:
                answer = answer + 1
            elif doki == 3:
                answer = answer + 1
        if count == 5:
            count = 0
            i = i + 1

    return answer
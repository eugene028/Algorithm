def solution(alp, cop, problems):
    answer = 0
    for i in range(len(problems)):
        if alp < problems[0][0] | cop < problems[0][1]:
            alp = alp + problems[0][0] - alp
            cop = cop + problems[0][1] - cop
            answer = answer + max((problems[0][0] - alp),(problems[0][1] - cop))
        elif alp >= problems[i][0] | alp >= problems[i][1]:
            while (alp >= problems[i+1][0] and cop >= problems[i+1][1])






solution(10,10,[[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])


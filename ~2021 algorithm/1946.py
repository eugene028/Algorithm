T = int(input())
for _ in range(T):
    answer = 2
    dica = {}
    dicb = {}
    answer_list = []
    N=int(input())
    for i in range(N):
        a,b = map(int, input().split())
        dica[i] = a
        dicb[i]= (b)

    lista = sorted(dica, key = lambda x : dica[x])
    listb = sorted(dica, key=lambda x: dicb[x]) #사람의 순위 리스트

    answer_list.append(lista[0])
    answer_list.append(listb[0])
    for i in range(1, N):
        if lista[i] in answer_list:
            continue
        listc = []
        me = lista[i]
        num = listb.index(me)

        listc = listb[num:]
        for j in range(0, i):
            if lista[j] in listc:
                    answer = answer + 1
                    answer_list.append(me)
                    break

    for i in range(1, N):
        if listb[i] in answer_list:
            continue
        listc = []
        me = listb[i]
        num = lista.index(me)
        listc = lista[num:]
        for j in range(0, i):
            if listb[j] in listc:
                answer = answer + 1
                answer_list.append(me)
                break
    for j in range(0,len(answer_list)):
        num1 = lista.index(answer_list[j])
        num2 = listb.index(answer_list[j])
        for i in range(1,N):
            num3 = listb.index(lista[i])
            if i < num1 and num3 < num2:
                answer = answer -1

    print(answer)





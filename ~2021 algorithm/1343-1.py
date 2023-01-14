T=int(input())
for i in range(T):
    N=int(input())
    people = []
    for j in range(N):
        people.append(list(map(int,input().split())))

    people.sort()
    people_list = people[0][1]
    cnt = 1 #서류 1등은 무조건 합격!

    for j in range(len(people_list)):
        if temp > people[j][1]: #면접 점수가 temp가 더 높아야.
            cnt += 1
            temp = people[j][1] #1등으로 등록

    print(cnt)
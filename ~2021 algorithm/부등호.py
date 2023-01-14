n = int(input())  # 숫자 입력받음
op = input().split() #부등호 어떻게 할 것인지 입력받음
c = [False] * 10  #먼저 c의 목록을 False로 가득 채워넣는다.
mx, mn = "", ""  #출력할 숫자(최소. 최대) 그룹 만든다!

def possible(i, j, k):  #possible 함수인데, 진짜 비교되는 수가 클 때
    if k == '<':
        return i < j  # True가 반환되게 하고
    if k == '>':
        return i > j  #얘도 마찬가지로, 수를 맞게 썼의면 True 반환하게, 아니면 False 반환하게 한다.
    return True  # if 문의 아무곳에도 안들어가지면 True 일단 반환하게 한다.

def solve(cnt, s):
    global mx, mn  #일단 global 함수 써서 외부로부터 받아오게 한 후에
    if cnt == n + 1:  # 이것은 Recurse 되는 부분! n+1 인덱스가 되면 멈추게 한다.
        if not len(mn):  #이건 아직 이해 못하겠음 ㅋㅋ
            mn = s  # 어쨌든 s 문자열을 mn에 부여한다는 것
        else:
            mx = s  #이것은 큰 문자열을 mx에 부여한다는 것이고..
        return  # 함수 끝내기!
    for i in range(10): # 0부터 9까지 검사하는 함수이다.
        if not c[i]:  #c[i]는 False 였다. if not False는 True이니까 if True 이렇게 되는거 ! 그러니까 if문 돌아간다.
            if cnt == 0 or possible(s[-1], str(i), op[cnt - 1]): # 일단 첫번째가 0일수도 있다고 했으니 그거 돌리고 s[-1]는 비교당하는 수, str(i)는 s에 입력될 수겠지. 그런데 <<는 0에서 인덱스 한번 쓰여서 -1 해주는것
                c[i] = True  # 일단 True로 바꿔주고
                solve(cnt + 1, s + str(i))  #인덱스 추가, s에 추가 해주고 !
                c[i] = False  # 다시 False로 초기화 해주어야 한다.
solve(0, "")
print(mx)
print(mn)
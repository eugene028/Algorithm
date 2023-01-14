"""import sys
input=sys.stdin.readline
board=list(input())
j=0
def check4():
    global j
    checkx= len(tmp)-j
    if(checkx % 4 ==0 ):
        for i in range(j, checkx):
            tmp[i]='A'
    elif (checkx % 4 ==2):
        if (checkx <=2 ):
            for i in range(j,len(tmp)):
                tmp[i]='B'
        else:
            for i in range(j, j+(checkx//4)*4):
                tmp[i]='A'
            for i in range(j+(checkx//4)*4, len(tmp)):
                tmp[i]='B'
    else:
        print(-1)
    j=checkx

num=0
tmp=list()
for i in range(len(board)): #보드에 아무것도 들어오지 않을 때를 고려해야 할까.
    if(board[i]=='X'):
        tmp.append(board[i])
    elif(board[i]=='.'):
        check4()
        continue

check4()
for j in range(len(tmp)):
    print(tmp[j])
"""

board = input()

i=0
while True:
    if i==len(board):
        break
    if board[i:i+4] =='XXXX':
        i=i+4
        board = board.replace('X','A',4)
    elif board[i:i+2]=='XX':
        i=i+2
        board = board.replace('X','B',2)
    elif board[i]=='.':
        i=i+1
    else:
        board =-1
        break
print(board)






RT=[0,0]
CF=[0,0]
JM=[0,0]
AN=[0,0]

def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        if(choices[i] == 4):
            continue
        elif (choices[i] <= 3):
            calculate(survey[i][0],4-choices[i])
        elif (choices[i] >= 5):
            calculate(survey[i][1],choices[i]-4)
    for i in range(0,4):
        if(i==0):
            if(RT[0] > RT[1]):
                answer = answer + 'R'
            elif (RT[0] < RT[1]):
                answer = answer + 'T'
            else:
                answer = answer + 'R'
        elif (i==1):
            if (CF[0] > CF[1]):
                answer = answer + 'C'
            elif (CF[0] < CF[1]):
                answer = answer + 'F'
            else:
                answer = answer + 'C'
        elif (i==2):
            if (JM[0] > JM[1]):
                answer = answer + 'J'
            elif (JM[0] < JM[1]):
                answer = answer + 'M'
            else:
                answer = answer + 'J'
        elif (i==3):
            if (AN[0] > AN[1]):
                answer = answer + 'A'
            elif (AN[0] < AN[1]):
                answer = answer + 'N'
            else:
                answer = answer + 'A'
    return answer

def calculate(key, num):
    if(key == 'R'):
        RT[0] = RT[0] + num
    elif (key == 'T'):
        RT[1] = RT[1] + num
    elif (key == 'C'):
        CF[0] = CF[0] + num
    elif (key == 'F'):
        CF[1] = CF[1] + num
    elif (key == 'J'):
        JM[0] = JM[0] + num
    elif (key == 'M'):
        JM[1] = JM[1] + num
    elif (key == 'A'):
        AN[0] = AN[0] + num
    elif (key == 'N'):
        AN[1] = AN[1] + num

x= solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
print(x)
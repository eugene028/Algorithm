
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
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
import math
def timeCalculate(time):
    splitTime = time.split(":")
    time = int(splitTime[0]) * 60 + int(splitTime[1])
    return time

def feeCalculate(fees, time):
    if(time <= fees[0]):
        return fees[1]
    else:
        lastTime = time - fees[0]
        value = math.ceil(lastTime / fees[2])
        return fees[1] + value * fees[3]

def solution(fees, records):
    carInfo = {}
    parkTimeList =[]
    answer = []
    for i in records:
        splitInfo = i.split()
        if splitInfo[1] in carInfo:
            carInfo[splitInfo[1]].append(splitInfo[0])
        else:
            carInfo[splitInfo[1]] = [splitInfo[0]]

    sortedCarInfo = dict(sorted(carInfo.items()))

    for carInfo in sortedCarInfo.values():
        parkTime = 0
        length = len(carInfo)
        if length % 2 == 0: #짝수라면
            for i in range(length//2):
                parkTime = parkTime + (timeCalculate(carInfo[i * 2 + 1]) - timeCalculate(carInfo[i * 2]))
            parkTimeList.append(parkTime)
        else:
            for i in range(length//2):
                parkTime = parkTime + (timeCalculate(carInfo[i * 2 + 1]) - timeCalculate(carInfo[i * 2]))
            parkTime = parkTime + (timeCalculate("23:59") - timeCalculate(carInfo[length - 1]))
            parkTimeList.append(parkTime)

    for i in parkTimeList:
        answer.append(feeCalculate(fees, i))

    return answer
A, B = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list3 = list1 + list2
list3.sort()
answerlist = list(map(str, list3))
answer = " ".join(answerlist)
print(answer)
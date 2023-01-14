
n=input()
n.rstrip()
stack=[]

for a in n:
    if a=="(":
        stack.append("(")
    elif a=="[":
        stack.append("[")
    elif a=="]":
        temp=0
        while 1:
            if len(stack)==0:
                print(0)
                exit(0)
            elif stack.pop()=='(':
                print(0)
                exit(0)
            elif stack.pop()=="[":
                if temp==0:
                    temp=1
                stack.append(temp*3)
                break
            else:
                temp= temp + stack.pop()
    elif a==")":
        temp=0
        while 1 :
            if len(stack)==0:
                print(0)
                exit(0)
            elif stack.pop()=="[":
                print(0)
                exit(0)
            elif stack.pop()=="(":
                if temp==0:
                    temp=1
                stack.append(temp*2)
                break
            else:
                temp=temp+stack.pop()
answer=0
while len(stack)>0:
    if stack.pop() == "("or stack.pop =="[":
        print(0)
        break
    answer= answer+stack.pop()
print(answer)

"""
import sys
input = sys.stdin.readline

str = input().rstrip()
stack = []

for char in str:
    if char == '[':
        stack.append(-3)
    elif char == '(':
        stack.append(-2)
    elif char == ']':
        temp = 0
        while True:
            if len(stack) == 0:
                print(0)
                sys.exit(0)
            top = stack.pop()
            if top > 0:
                temp += top
            elif top == -2:  # top was (
                print(0)
                sys.exit(0)
            elif top == -3:
                if temp == 0:  # temp has not been changed
                    temp = 1
                stack.append(temp * 3)
                break;
    elif char == ')':
        temp = 0
        while True:
            if len(stack) == 0:
                print(0)
                sys.exit(0)
            top = stack.pop()
            if top > 0:
                temp += top
            elif top == -3:  # top was [
                print(0)
                sys.exit(0)
            elif top == -2:
                if temp == 0:  # temp has not been changed
                    temp = 1
                stack.append(temp * 2)
                break

answer = 0
while len(stack) > 0:
    top = stack.pop()
    if top < 0:
        print(0)
        sys.exit(0)
    answer += top
print(answer)
"""

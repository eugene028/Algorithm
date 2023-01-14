#include<iostream>
#include<cstring>
result=0;
word=input()
i=0
num=len(word)


for i in range(num-1,-1,-1):
    num2=0
    if word[i]=='A':
        num2=10
    elif word[i]=='B':
        num2=11
    elif word[i]=='C':
        num2=12
    elif word[i]=='D':
        num2=13
    elif word[i]=='E':
        num2=14
    elif word[i]=='F':
        num2=15
    else:
        num2=int(word[i])

    result= result+num2*(16**(num-1-i))

print(result)

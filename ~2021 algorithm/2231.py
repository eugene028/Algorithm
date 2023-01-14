num = int(input())
result = 0
check = 1
checkbox = 1

while (checkbox < num):
    check = checkbox
    while(check):
        result = result + check % 10
        check = check / 10
    result = result + checkbox
    if (num == result):
        print(check)
    checkox = checkbox + 1
if(checkbox == result):
    print(0)
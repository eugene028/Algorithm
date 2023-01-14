import sys
from collections import deque
input=sys.stdin.readline

for _ in range(int(input())):
    r=False
    p=input()
    n=int(input())
    l=list(input()[1:-2].split(','))

    d=(deque() if n==0 else deque(l))
    try:
        for i in p:
            if i=="R":
                r = not r
            elif i =="D":
                if d:
                    d.pop() if r else d.popleft()
                else:
                    print("error")
                    raise Exception
    except Exception:
        continue
    if r:
        d.reverse()
    print('['+','.join(map(str,d))+']')
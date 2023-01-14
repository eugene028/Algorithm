
import sys
input=sys.stdin.readline

def mytime(t):
    a,b=map(int,t.split(":"))
    return a*100 +b
s,e,q=map(mytime,input().split())
my=set()
person=0
for j in sys.stdin:
    try :
        p,a= j.split()
    except:
        break
    p=mytime(p)
    if p<=s:
        my.add(a)
    elif e<=p<=q:
        if a in my:
            my.remove(a)
            person+=1
print(person)

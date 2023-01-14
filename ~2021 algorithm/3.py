a=input()
result=1
d=list(x for x in range(1,11))
d.reverse()
c=list(x for x in range(1,27))
c.reverse()

for i in range(len(a)):
    if a[i]=="d":
        for j in range(len(d)):
            if a[i]==a[i+1]:
                result=result*d[j]
            if a[len(a)-1]:
                break
            if a[i]!=a[i+1] :
                break
            result = result * d[j]
    if a[i]=="c" and a[i]==a[i+1]:
        for j in range(len(c)):
            result=result*c[j]
            if a[i]!=a[i+1] or a[len(a)-1]:
                break

print(result)
"""
for i in a:
    if i =="d":
        if i==i+1:
            for j in range(len(d)):
                result=result*d[j]
        else:
            for j in range(len(d)):
                result=result*d[j]
                break
    if i=="c":
        if i==i+1:
            for j in range(len(c)):
                result=result*c[j]
        else:
            for j in range(len(d)):
                result=result*d[j]
                break

print(result)
"""
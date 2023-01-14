a=input()
result=[]
for j in a:
    if j=="c":
        result.append(26)
    if j=="d":
        result.append(10)
ans=result[0]
for k in range(1,len(result)):
    if result[k-1]==result[k]:
        ans=ans*(result[k]-1)
    else:
        ans=ans*result[k]
print(ans)


'''
a=input()
d=list(x for x in range(1,10))
d.reverse()
c=list(x for x in range(1,26))
c.reverse()

for i in range(1,len(a)):
    if a[i]=="d":
        if a[0]:
            result=10
        if a[i-1]==a[i]:

        for j in range(len(d)):
            if a[i-1]==a[i] :
                result = result * d[j]
            if a[i]=="c" or i==len(a):
                break

    if a[i]=="c":
        if a[0]:
            result=26
        for j in range(len(c)):
            result = result * c[j]
            if a[i]=="d":
                break
            if a[len(a)-1]:
                break

print(result)
'''
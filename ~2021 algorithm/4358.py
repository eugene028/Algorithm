""""
import sys
input=sys.stdin.readline
list1=[]
list2=[]
total=0
for j in sys.stdin:
    if j =="\n":
        break
        list1.append(j)
        list2.append(1)
    elif j in list1:
        list2[list1.index(j)]+=1

for i in sorted(list1):
    print("{} {:4f}".format(i,format(i,(list2[list1.index(i)]/total)*100)))

"""
import sys
from collections import defaultdict
total=0
dc=defaultdict(int)
for line in sys.stdin:
    if line == "\n":
        break
    line=line.rstrip()
    total+=1
    dc[line]+=1
st=list()
for item in dc.items():
    st.append([item[0],item[1]/total*100])
st.sort()
for item in st:
    print(item[0],"%.4f" % item[1])

from itertools import combinations

n=int(input())
s=list(input().split())
k=int(input())

c=list(combinations(s,k))
#print(c)
d=0
for i in c:
    if(i.__contains__('a')):
        d=d+1
#print(d)

print((d/len(c)))



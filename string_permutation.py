from itertools import permutations
s,n=input(),int(input())

c=sorted(list(permutations(s,n)))
#print(c)

for i in c:
    s1=''
    for j in range(len(i)):
        s1=s1+i[j]
    print(s1)
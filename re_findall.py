import re

s=input()
l2=['a','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
matcher=re.finditer('[aeiouAEIOU]',s)
l1=list()
for match in matcher:
    l1.append((match.start(),match.group()))
print(l1)
s1=''
for i in range(0,len(l1)):
    j=i+1
    if(j<len(l1)):
        if(l1[i][0]+1==l1[j][0]):
            if(s[l1[i][0]-1] in l2):
                s1=s1+l1[i][1]
print(s1)
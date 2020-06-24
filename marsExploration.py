import os
import sys


s="SOSSOSSOSSOS"
def marsExploration(s):
    #print(s)
    s1="SOS"
    l=len(s)
    #print(l)

    s2=""
    while(l>0):

        for i in range(0,len(s1)):
            s2=s2+s1[i]
            l=l-1
            if(i==len(s1)):
                i=0
    #print(s2)
    c=0
    for i in range(0,len(s2)):
        j=i
        if(s2[i]!=s[j]):
            c=c+1
    return(c)
result=marsExploration(s)
print(result)
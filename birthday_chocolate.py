import os
import sys


s=[2 ,5 ,1 ,3 ,4 ,4 ,3 ,5 ,1 ,1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2 ,1]
m=7
d=18
def birthday(s, d, m):
    c=0

    if(len(s)==1 and s[0]==d):
        c=c+1
    else:
        i=0
        e=0
        sum=0
        for x in range(i,len(s)):
            print("i=",i)
            if(x+1!=len(s)):
                sum=sum+s[x]
                print("sum=",sum)
                e=e+1
                if(e==m):
                    print("e=",e)
                    if(sum==d):
                      c=c+1
                      i=i-5
                      sum=0
                      e=0
                    else:
                        i = i -5
                        sum = 0
                        e = 0
                else:
                    i=i+1


    return c

t= birthday(s, d, m)
print(t)
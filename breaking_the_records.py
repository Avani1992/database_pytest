import os
import sys

scores=[10 ,5 ,20 ,20 ,4 ,5 ,2 ,25 ,1]
def breakingRecords(scores):
    max=scores[0]
    min=scores[0]
    c=0
    d=0
    for x in range(1,len(scores)):
        if(scores[x]>max):
            max=scores[x]
            c=c+1
        elif(scores[x]<min):
            min=scores[x]
            d=d+1
        else:
            pass
    return (c,d)


t=breakingRecords(scores)
print(t)

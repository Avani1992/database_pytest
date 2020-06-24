import os
import sys

arr=[2]
brr=[20,30,12]


def getTotalX(a, b):
    l1 = list()
    l2 = list()

    for x in range(1,(b[0]+1)):
        c = 0
        for y in a:
          if(x%y==0):
              c=c+1

        if(x not  in l1 and c==len(a)):
                l1.append(x)

    print(l1)
    for x in l1:
        d=0
        for y in b:
            if(y%x==0):
                d=d+1
        if(x not in l2 and d==len(b)):
                   l2.append(x)

    print(l2)
    return len(l2)


total = getTotalX(arr, brr)
print(total)
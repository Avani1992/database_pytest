import math
import os
import random
import re
import sys

s = "ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges"


def sherlockAndAnagrams(s):
    l1 = list()
    l2=list()
    for i in range(0, len(s)):
        current = s[i]
        sliced = s[i + 1:]
        for j in sliced:
            if (current == j):
                l1.append((current, j))


    m=0
    k=m+1
    k1=k+1
    s1 = s[m] + s[k]
    s2 = s[k] + s[m]
    s3=s[m]+s[k]+s[k1]
    s4=s[k]+s[k1]+s[m]
    s5=s[k1]+s[m]+s[k]
    s6=s[m]+s[k1]+s[k]
    s7=s[k]+s[m]+s[k1]
    s8=s[k1]+s[k]+s[m]
    sliced=s[k:]
    if((s1 in sliced) ):
         l1.append((s1,s1))
         l1.append((s2, s1))
    if(s2 in sliced):
        l1.append((s1,s2))


    if((s3 in sliced)):
        l1.append((s3,s3))
    elif((s4 in sliced)):
        l1.append((s3,s4))
    elif ((s5 in sliced)):
        l1.append((s3, s5))
    elif ((s6 in sliced)):
        l1.append((s3, s6))
    elif ((s7 in sliced)):
        l1.append((s3, s7))
    elif ((s8 in sliced)):
        l1.append((s3, s8))

    print(len(l1))
    return (l1)




result = sherlockAndAnagrams(s)
print(result)

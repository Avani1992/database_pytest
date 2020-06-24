import os
import sys

class split_line:
    each=['a','b','c']
    s2=""
    for j in each:
        s2=s2+j+','
    print(s2)
    with open('failure_wp.log','r') as file1:
           data=file1.readlines()
           print(data)

           s1=""
           for i in data:
               if(i.endswith('.py')):
                  s1=s1+i
           print(s1)
           file1.close()
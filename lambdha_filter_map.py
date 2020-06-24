import os
import sys
import functools

def cube(y):
    return y*y*y
print(cube(5))

a=lambda x: x*x*x  # Expression is the return statement for lambda()
print(a(5))

b=lambda x,y:(x+y)  # Take x=3 and y=4 and return 7 as a ans.
print(b(3,4))

l=[2,3,4,12,6,7,34]
sort_list=list(filter(lambda x:(x%2==0),l))  # filter the even no. and make a list of that no. Filter returns only that no. which is even(condition for filter is True for those no.)
print(sort_list)

l1=[1,2,3,4]
sqrt_list=list(map(lambda x:x*x,l1))
print(sqrt_list)

l2=[2,45,3,1,67,42]
reduce_list=functools.reduce((lambda x,y:x+y),l2)
print(reduce_list)


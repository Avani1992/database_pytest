"""
WAP which will create a tuple of 3 random numbers between (1,10). Create 10 differnet tuples like this in a list.
filter out lists which have all elements entries are odd.

[rand,rand,rand]

Example: created a list via random function is [[1,1,1],[2,9,8],[3,3,7].....]
filter[[1,1,1],[3,3,7]] etc...


Author : Avani Patel
"""
import os
import sys
import random

class random_list:

    def random_no(self,a,b):
        self.res=list()
        for i in range(10):
            self.res.append((random.randrange(a,b),random.randrange(a,b),random.randrange(a,b)))
        print("res = ",self.res)
        self.random_filter=list(filter(lambda  x:((x[0]%2!=0) and (x[1]%2!=0) and (x[2]%2!=0) ),self.res))
        print("random_filter: ",self.random_filter)



obj=random_list()

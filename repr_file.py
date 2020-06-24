import os
import sys

class repr_file:
    globalSt = [90,12,222,122,22]
    tp = 90
    ko= 80
    def __init__(self, real):
        self.real = real
    def __repr__(self):
        return '[%s]' %(self.real)
    def __str__(self):
        return '%s %s %s'% (repr_file.globalSt,repr_file.tp,repr_file.ko )


r = repr_file("csdcidsic")
print(r)

# print(r.globalSt)

"""
when str and repr both the methods are there, then bydefault str() called. 
but if we want the o/p in form of repr() then we have to write repr(objectname).
"""
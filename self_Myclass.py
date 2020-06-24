import os
import sys

class self_Myclass:
    k=10
    def method(self):
        self.m=20
    def update(self,n):
        self.m=self.m+n
        self_Myclass.k=60
    def print1(self):
         print("updated value of instance variable is:",self.m)
         print("updated value of class variable is:", self_Myclass.k)


obj=self_Myclass()
obj1=self_Myclass()
obj.method()
obj1.method()

# obj.print1()
# obj1.print1()
obj.update(10)
# obj.print1()
# obj1.print1()

self_Myclass.k=90
# obj.print1()
# obj1.print1()

obj.m=50   # reflect only in obj.print1()
obj1.m=60  # reflect only in obj1.print1()
# obj.print1()
# obj1.print1()

obj.k=-1
obj.print1()
obj1.print1()

self_Myclass.k=-5
obj.print1()
obj1.print1()

"""
we can change the instance variable using objects is not reflected to all objects. this changes only for that object only using which object we change 
the variable. using class name we can change the class variable which is reflected to all the objects.

"""


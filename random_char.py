"""
generate random characters out of [a-z]
{'India', 'Hindustan','hindu','Hockey','Lion'} WAP to print any of the entry randomly.

"""
import os
import sys
import random


class random_char:
    def charlist(self,l):
        self.l1=list()
        for i in range(10):
            self.l1.append(l[(random.randint(0,25))])
        print("Random char is: ",self.l1)
    def setlist(self,s):
        print("country is: ",random.choices(s))

l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# s={'India', 'Hindustan','hindu','Hockey','Lion'}
print(dir(random))
obj=random_char()
obj.charlist(l)
# obj.setlist(s)
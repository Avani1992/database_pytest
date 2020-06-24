import os
import sys
"""
sys.argv pass the list as a argument. sys.argv give us the arguments inform of list.
first element in list is Filename(eg. CLI_argu_sum.py) and then after rest of the argument which we pass from the CLI.
All the elements in the list is in String form only. If we want integer value we have to convert it in int().
"""
class CLI_argu_sum:
    def arg_sum(self,a):  # here a=["CLI_argu_sum.py",'5','4','Good girl she is'] pass from (sys.argv)
        self.sum=0
        # for i in range(1,len(a)):
        #     self.sum=self.sum+int(a[i])
        self.sum=int(a[1])+ int(a[2])
        print("Sum is: ",self.sum)
    def split_word(self,s):
        print(s)
        self.l1=s[3]
        self.s1=self.l1.split(' ')
        for i in self.s1:
            print("Word is: ",i)
obj=CLI_argu_sum()
obj.arg_sum(sys.argv)
obj.split_word(sys.argv)

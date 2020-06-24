import os
import sys

class filter_freehand_magic:
    # l=[[1,2,3,900,3,2,1],[1,2,1,5,3,2,1],[1,4,1],[234,456,678,999,678,456,234],[0,0,1,0,1,0,0],[-1,-1,-1],[21,33,21,33],[0,0,0,0,0]]

       def magic(self,l):
         self.l1=list()
         for i in l:
           if (len(i) % 2 != 0):
                self.l1.append(i)
         print("List1 is: ",self.l1)

         # for i in self.l1:
         #    l2=int(len(i)/2)
         #    self.front=i[0:l2]
         #    self.back=i[(l2+1):]
         #    #    print("list",i)
         #    # print("Front is: ",self.front)
         #    #print("Back is: ",self.back)
         #    self.back=list(reversed(self.back))
         #    #print("reverse: ",self.back)
         #    #if(self.front==self.back):
         #    #    print(i)
         self.magic_list=list(filter(lambda x:(x==list(reversed(x))),self.l1))
         print("Magic_list : ",self.magic_list)


l=[[1,2,3,900,3,2,1],[1,2,1,5,3,2,1],[1,4,1],[234,456,678,999,678,456,234],[0,0,1,0,1,0,0],[-1,-1,-1],[21,33,21,33],[0,0,0,0,0]]
obj=filter_freehand_magic()
obj.magic(l)

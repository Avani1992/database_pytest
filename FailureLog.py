import os
import sys
import json

"""
Expectation: get .txt .sh .py files ad write them up into JSON formatted file.
"""


class FailureLog:


    with open('failure_wp.log','r') as file1:
           data=file1.readlines()
           t = [i[:-1] for i in data]
           data = t
           file1.close()

    def file_py(self,m):
         self.l1=list()
         self.d=dict()
         for each in FailureLog.data:
           self.s2=each.split(' ')
           for j in self.s2:
             if(j.endswith(m)):
                 self.l1.append(j)
         self.d[m]=self.l1
    def file_sh(self,m):
         self.l1=list()
         self.d=dict()
         for each in FailureLog.data:
           self.s1=each.split(' ')

           for j in self.s1:
            if(j.endswith(m)):
              self.l1.append(j)
         self.d[m]=self.l1
    def file_txt(self,m):
         self.l1=list()
         self.d=dict()  # every time dict is empty.
         for each in FailureLog.data:
             self.s1 = each.split(' ')

             for j in self.s1:
               if(j.endswith(m)):
                 self.l1.append(j)
         self.d[m]=self.l1
    def print1(self):
        with open("FileFormat.json","a") as File1:
            json.dump(self.d,File1)  #every time new dict is created. when calling that method. so dict's key-value pair new created.
        File1.close()
        print(" File:",self.l1)


log_py=FailureLog()
log_py.file_py('.py')
log_py.print1()

log_txt=FailureLog()
log_txt.file_py('.txt')
log_txt.print1()

log_sh=FailureLog()
log_sh.file_py('.sh')
log_sh.print1()




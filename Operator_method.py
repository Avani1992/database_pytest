import os
import sys
import json
import ast

class Operator_method:
    with open("operator.json","r") as File2:
        data1=json.load(File2)
    print(data1)
    # with open("operator.json") as File2:
    #     data=ast.literal_eval(File2.read())
    # print(data)

    File2.close()
    def sum_method(self,a,b):
        self.sum=0
        self.sum=a + b
        print("Sum is: ",self.sum)
    def division_method(self,a,b):
        self.div = 1
        self.div =a / b
        print("Division is: ", self.div)
    def mul_method(self,a,b):
        self.mul=1
        self.mul = a * b
        print("Multiplication is: ", self.mul)
    def sub_method(self,a,b):
        self.sub=0
        self.sub = abs(sa - b)
        print("Subtraction is: ", self.sub)
    def modulus_method(self,a,b):
        self.mod=1
        self.mod =a % b
        print("Modulus is: ", self.mod)
    def sort_method(self,j):
        j.sort()
        print("Sorted list is: ",j)


obj1=Operator_method()
for i, j in obj1.data1.items():
    if (i == "sum"):
        a=j[0]
        b=j[1]
        obj1.sum_method(a,b)
    if(i=="modulus"):
        a=j[0]
        b=j[1]
        obj1.modulus_method(a,b)
    if (i == "division"):
        a = j[0]
        b = j[1]
        obj1.division_method(a,b)
    if (i == "multi"):
        a = j[0]
        b = j[1]
        obj1.mul_method(a,b)
    if (i == "subtract"):
        a = j[0]
        b = j[1]
        obj1.sub_method(a,b)
    if (i == "sort"):
        obj1.sort_method(j)
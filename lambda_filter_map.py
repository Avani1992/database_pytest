# from functools import reduce
# l1=[1,2,3,4]
#
# l2=lambda x:x*x
# print(l2(5))
#
# l3=list(map((lambda x:x*2),l1))
# print(l3)
#
# l4=list(filter((lambda x:x%3==0),l3))
# print(l4)
#
# l5=reduce(lambda x,y:x+y,l1)
# print(l5)

# from fractions import Fraction
# from functools import reduce
# import operator
#
# fracs=[Fraction(1,2),Fraction(3,4),Fraction(10,6)]
# def product(fracs):
#     t =reduce(lambda x,y: x*y, fracs)  # complete this line with a reduce statement
#     return t.numerator, t.denominator
#
# result = product(fracs)
# print(result)

# x,k=map(int,input().split())
#
# print(x)
# print(k)
#
# if((x**3 + x**2 + x + 1)==k):
#     print (True)
#
# ui = input().split()
# x = int(ui[0])
# print(eval(input()) == int(ui[1]))

eval(input())

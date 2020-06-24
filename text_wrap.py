"""You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w."""

import textwrap
s='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w=4
# def wrap(string, max_width):
#     s1=''
#     c=0
#
#     for i in string:
#         s1=s1+i
#         c=c+1
#         if(c==max_width):
#             print(s1)
#             s1=''
#             c=0
#
#     return s1
#
#
#
# result=wrap(s,w)
# print(result)

n = 17
width = len(format(n))
print(width)
for i in range(1,n+1):
  print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     l1=list()
#     for k in range(1,i):
#         l1.append(k)
#     l2=l1[::-1]
#     for p in l2:
#         print(p,end='')
#
#     print()

#2.-----------------------------------
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

#
# import numpy
#
# my_array=numpy.array([[int(input()),int(input())],[int(input()),int(input())]])
#
# print(numpy.sum(my_array,axis=0))
# c=numpy.sum(my_array,axis=0)
# print(c)
# --------------------------------------------------------
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print(integer_list)
#     l1=tuple(integer_list)
#     print(hash(l1))
#
#   ---------------------------------------------------------

# import numpy
#
# n=int(input())
# A=numpy.array([input().split() for _ in range(n)],float)
#
# print(numpy.linalg.det(A))

#-------------------------------------------------
# from collections import defaultdict
#
# d=defaultdict(list)
# n,m=map(int,input().split())
#
# for i in range(1,n+1):
#     s=input()
#
#     d[s].append(i)
#
#
#
# l1=list()
# for i in range(1,m+1):
#     s=input()
#     l1.append(s)
# for i in l1:
#     if(i in d):
#         print(' '.join(map(str,d[i])))
#     else:
#         print("-1")

#-------------------------------------------------

# from collections import namedtuple
#
# n = int(input())
#
# categories = input().split()
# data = namedtuple('data', categories)
# marks=list()
# for i in range(n):
#     marks.append(int(data._make(input().split()).MARKS))
# print(marks)
# print((sum(marks))/len(marks))

#--------------------------------------------------
# from collections import OrderedDict
#
# data=OrderedDict()
# c=0
# for i in range(int(input())):
#     s=input().rpartition(" ")
#
#     if(s[0] in data):
#
#         data[s[0]]=data[s[0]]+int(s[-1])
#     else:
#         data[s[0]]=int(s[-1])
#
# #print(data)
#
# for i,v in data.items():
#     print(i,v)

#-----------------------------------------------
# from collections import OrderedDict
#
# data=OrderedDict()
# for i in range(int(input())):
#     s=input()
#     if(s in data):
#         data[s]=data[s]+1
#     else:
#         data[s]=1
# #print(data)
# print(len(data))
# for k,v in data.items():
#     print(v,end=' ')

#------------------------------------------------------
# from collections import Counter
#
# n=int(input())
# arr=list(map(int,input().split()))
# c=Counter(arr)
# #print(c)
# sum=0
# for i in range(int(input())):
#         s=list(map(int,input().split()))
#         if(s[0] in c.keys()):
#             if(c[s[0]]>0):
#                 c[s[0]]=c[s[0]]-1
#                 sum=sum+s[1]
#                 #print(c)
#             else:
#                 pass
#         else:
#             pass
# print(sum)

#------------------------------------------
# xml=''
# for _ in range(int(input())):
#     xml=xml+input()
# import xml.etree.ElementTree as etree
# tree = etree.ElementTree(etree.fromstring(xml))
# sum=0
# def traverse(node):
#     len12=0
#     sum=1
#     return len(node.attrib) + sum(traverse(child) for child in node)
#     # for child in node:
#     #     len12=len(child.attrib)
#     #     print(child,' ',len12)
#     #     sum=sum+len12
#     # return sum


#
# print(traverse(tree.getroot()))

#------------------------------------------
n,m=map(int,input().split())
l1=list()
for i in range(n):
    l1.append(list(map(int,input().split())))
#print(l1)
k=int(input())
temp=0
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if(l1[i][k]>l1[j][k]):
            temp=l1[j]
            l1[j]=l1[i]
            l1[i]=temp
#print(l1)
for i in l1:
    for j in i:
        print(j,end=' ')
    print()



"""Captal the first name and lastname first characer."""

s='hello world lol'
# def solve(s):
#     l1=list()
#     l1=s.split( )
#     print(l1)
#     s1=''
#     s2=''
#     l2=list()
#     for i in l1:
#         size=len(i)
#         s1=i[0].upper()+i[1:]
#         l2.append(s1)
#         s2=s2+' '+s1
#     return s2.lstrip()
# result=solve(s)
# print(result)

def solve(s):
    s1=''
    for i in range(0,len(s)):
        if(i==0  or s[i-1].isspace()):
            s1=s1+s[i].upper()

        else:
            s1=s1+s[i]

    return s1.lstrip()
result=solve(s)
print(result)

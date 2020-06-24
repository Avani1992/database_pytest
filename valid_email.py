# """It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is 3."""
#
#
# emails=[
#     'iu89_in.plus @ google.com'
#     ,'ill @ google.com'
#     ,'fill @ google1.com'
# ]
# import re
#
# def fun(s):
#     l1=list()
#     l1=s.split('@')
#     #print(l1)
#     count=0
#     if(len(l1)>1):
#         if( ' ' in l1[0] or l1[0].isalnum()==True or '_' in l1[0] or '-' in l1[0]):
#
#                 count=count+1
#
#         l2=l1[1].split('.')
#
#         if(len(l2)==2):
#             if(l2[0].isalnum() or ' ' in l2[0]):
#                 count=count+1
#
#             if(len(l2[1])<=3):
#                 count=count+1
#
#
#
#     if(count==3):
#         return True
#     else:
#         return False
#         # return True if s is a valid email, else return False
#
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
#
#
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

import re
n=int(input())
for _ in range(n):

    s = input()

    x = s.split()
    print(x)
    if len(x) > 1 and '{' not in x:
        x = re.findall(r'#[a-fA-F0-9]{3,6}', s)
        [print(i) for i in x]
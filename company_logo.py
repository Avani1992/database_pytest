"""A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition. Given a string ,
which is the company name in lowercase letters, your task is to find the top three most common characters in the string."""

s='aabbbccde'
d=dict()
for i in s:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
l1=list(d.keys())
k=0
print(l1)
l2=list(d.values())



print('d1',l3)



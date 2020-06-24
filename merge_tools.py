""""""
s='AABCAAADA'
k=3
def merge_the_tools(s, k):

    length=len(s)
    size=int(length/k)
    #print(size)
    s1=s[0]

    for i in range(1,length+2):
        if(i%3!=0):
            if(s[i] not in s1):
                s1=s1+s[i]
            else:
                pass
        else:
            print(s1)
            if(i<length):
                s1=''
                s1=s[i]

            else:
                break



merge_the_tools(s,k)

for part in zip(*[iter(s)] * k):
    print(part)
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
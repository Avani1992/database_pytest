for i in range(int(input())):
    n=int(input())
    l1=list(map(int,(input().split())))


    d=dict()
    for i in l1:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1


    c=list()
    for k,v in d.items():
        if(v%2!=0):
            c.append(k)
    print(c)
    c=sorted(c)
   # print(c[0],c[1])
    #c = sorted(c)
    if (len(c) == 2):
        print(c[0], c[1])
    else:
        print(c[0])


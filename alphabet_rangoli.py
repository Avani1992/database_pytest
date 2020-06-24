l1=['a','b','c','d','e','f','g','h','i','j']
n=5
k=1
# for i in range(1,n+1):
#     for j in range(k,n+1):
#         print(end='-')
#     k=k-2
#     d=0
#     for l in range(0,i):
#         d=n-1
#         print(l1[d],end=' ')
#         n=n-1
#     print()
k=(n-1)*2
for i in range(1,n+1):
    for j in range(k):
        print(end="-" )

    d=0
    s=n
    for j in range(0,i):
        d=s-1
        print(l1[d],end="-")
        s=s-1

    for j in range(0,i-1):
        d=s+1
        print(l1[d],end="-")
        s=s+1
    for j in range(k):
        print(end="-" )
    k=k-2
    print()

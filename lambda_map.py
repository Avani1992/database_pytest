cube = lambda x: x*x*x

n=5
def fibonacci(n):
    l1=list()

    for i in range(0,n):
        if(len(l1)==0):
            l1.append(i)
        elif(len(l1)==1):
            l1.append((l1[i-1]+i))
        else:
            l1.append((l1[i-2]+l1[i-1]))
    print(l1)
    return l1


print(list(map(cube, fibonacci(n))))
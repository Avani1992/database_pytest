def ReturnMe(arg):
    a = 90
    b = arg

    yield 12
    yield 13
    yield 2
    yield 3


# Driver code to check above generator function
for value in ReturnMe(23):
    print(value)
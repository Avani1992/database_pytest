def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

seq =['a','r','i','t','y','o','u','e','w','u']
nums = [1,2,3,4,5,6,7,8,9]

# filtered = filter(fun,seq)
filteredOdd = filter(lambda x: x%2, nums)
filteredEven = filter(lambda x: x%2==0, nums)

print(filteredOdd.__next__())
print(filteredOdd.__next__())
print(filteredOdd.__next__())
print(filteredOdd.__next__())
print(filteredOdd.__next__())
print(filteredEven.__next__())
print(filteredEven.__next__())
print(filteredEven.__next__())
print(filteredEven.__next__())

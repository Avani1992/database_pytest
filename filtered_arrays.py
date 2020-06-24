import copy

def checkSorted(arr):
    t= copy.deepcopy(arr)
    arr.sort()
    if t == arr:
        return True
    else:
        return False

def checkMagical(arr):
    first = 0
    last = -1
    while(arr[first] == arr[last]):
        if(first == int(len(arr)/2)+1):
            return True
        else:
            first = first +1
            last = last -1
    return False

arr = [[1,2,3,6,9],[3,4,5,1,2],[33,45,66,77],[-1,-0,45,67],[123,333,444,90]]
arr1= [[1,2,3,0,3,2,1],[123,234,456,234,123],[34,34,45,34,34,0,34],[3,3,4,4,5,5,3,3,3]]
# filtered = filter(checkSorted,arr)
filtered = filter(checkMagical,arr1)
print(filtered.__next__())
print(filtered.__next__())

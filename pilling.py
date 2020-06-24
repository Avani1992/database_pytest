"""There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should follow these directions: if  cube(i) is on top of cube(j) then  sidelength(j)>=sidelength(i).

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks."""

for t in range(1):
    input()
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print ("Yes" if i == l - 1 else "No")
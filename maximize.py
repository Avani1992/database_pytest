"""you have give a different list. pick one element from each list and make sum of all elements square.and modulo it by M"""
from itertools import product
n,M= map(int,input().split())



l1=(list(map(int,input().split()))[1:] for _ in range(n))
#print(l1)
results = map(lambda x: sum(i**2 for i in x)%M, product(*l1))
print(max(results))


l1=[['24'],['25'],['27']]

res=[ int(j) for i in l1 for j in i]

for k in res:
    print(k)

res=[ [int(j1) for j1 in j] for i in l1 for j in i]

for k in res:
    print(k)
    
    

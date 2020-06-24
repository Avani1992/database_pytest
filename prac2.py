l1 = [1,3,4,15,19]
l2 = [7,2,5,4,3,6,1,9,10,12]
count = 0
l4=l1.sort()
for i in range(0, len(l1)):

    for j in range(i + 1, len(l1)):
        if ((l1[i] + l1[j]) in l1):
            count = count + 1

if (count > 0):
    print(count)
else:
    print(-1)

count1 = 0
for i in range(0, len(l2)):

    for j in range(i + 1, len(l2)):
        if ((l2[i] + l2[j]) in l2):
            count1 = count1 + 1

if (count1 > 0):
    print(count1)
else:
    print("-1")

print(sorted(l1))

"""You are given a string S.
 S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits."""

s='Sorting1234'
l1=sorted(s)
print(l1)
lower=''
upper=''
odd1=''
even1=''
for i in l1:
    if(i.islower()):
        lower=lower+i
    elif(i.isupper()):
        upper=upper+i
    elif(i.isdigit()):
        if(int(i)%2!=0):
            odd1=odd1+i
        else:
            even1=even1+i

    else:
        pass
print(lower+upper+odd1+even1)
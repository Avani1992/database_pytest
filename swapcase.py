"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa"""

s='HackerRank.com presents "Pythonist 2".'
def swap_case(s):
    s1=''
    for i in range(0,len(s)):
        if(s[i].islower()):
            s1=s1+s[i].upper()
        elif(s[i].isupper()):
            s1=s1+s[i].lower()
        else:
            s1=s1+s[i]
    return s1

result=swap_case(s)
print(result)
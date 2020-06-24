"""Game Rules

Both players are given the same string,S .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings."""

s='BANANANAAAS'
def minion_game(string):
    s=string.lower()
    l1=['a','e','i','o','u']
    d=dict()
    d1=dict()
    for i in s:
        if(i in l1):
            if(i in d1):
                d1[i]=d1[i]+1
            else:
                d1[i]=1
        else:
            if(i in d):
                d[i]=d[i]+1
            else:
                d[i]=1

    for i in range(0,len(s)):
        s1=s[i]
        for  j in range(i+1,len(s)):
            if(s[i] not in l1):
                s1=s1+s[j]
                if(s1 in d):
                    d[s1]=d[s1]+1
                else:
                    d[s1]=1
            else:
                s1=s1+s[j]
                if (s1 in d1):
                    d1[s1] = d1[s1] + 1
                else:
                    d1[s1] = 1

    st=sum(d.values())
    kevin=sum(d1.values())
    print(st)
    print(kevin)
    if(st>kevin):
        print("Stuart",st)
    elif(st==kevin):
        print("Draw")
    else:
        print("Kevin",kevin)



minion_game(s)
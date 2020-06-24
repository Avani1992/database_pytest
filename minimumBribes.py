"""It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person
 wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same
 sticker denoting their original places in line. One person can bribe at most two others.
 For example, if  n=8 and Person5 bribes Person4 , the queue will look like this:1,2,3,5,4,6,7,8 .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!"""

q=[1 ,2 ,5 ,3 ,7 ,8 ,6 ,4]
# s1=0
# c=0
# d=dict()
# def minimumBribes(q):
#     for i in range(0,len(q)+1):
#         j=i+1
#         if(j<len(q)):
#             if(q[i]>q[j]):
#
#                 s1=q[j]
#                 q[j]=q[i]
#                 q[i]=s1
#                 if(q[j] in d and q[i] in d):
#                     d[q[j]]=d[q[j]]+1
#                     d[q[i]]=d[q[i]]+1
#                 else:
#                     d[q[j]]=1
#                     d[q[i]]=1
#             print(q)
#             print(q[i])
#             if(q[i-1]>q[i] and i!=0):
#                 s1 = q[i]
#                 q[i] = q[i-1]
#                 q[i-1] = s1
#                 if (q[i] in d and d[q[i-1]] in d):
#                     d[q[i]] = d[q[i]] + 1
#                     d[q[i-1]]=d[q[i-1]]+1
#                 else:
#                     d[q[i]] = 1
#                     d[q[i-1]]=1
#             if (q[i - 1] > q[i] and i != 0):
#                 s1 = q[i]
#                 q[i] = q[i - 1]
#                 q[i - 1] = s1
#                 if (q[i] in d and d[q[i - 1]] in d):
#                     d[q[i]] = d[q[i]] + 1
#                     d[q[i - 1]] = d[q[i - 1]] + 1
#                 else:
#                     d[q[i]] = 1
#                     d[q[i - 1]] = 1
#
#     print(q)
#     print(d)
#     max1=0
#     max1=max(d.values())
#     if(max1>2):
#         print("Too chaotic")
#     else:
#         print(sum(d.values()))
#
#
#
# minimumBribes(q)

q=[1 ,2 ,5 ,3 ,7 ,8 ,6 ,4]
def minimumBribes(q):
    l1=list()
    s1=0
    length=len(q)
    for i in range(1,length+1):
        l1.append(i)
    print(l1)
    for i in range(0,len(l1)):
        if(l1[i]==q[i]):
            pass
        else:
            j=i+1
            if(j<len(q)):
                s1=q[j]
                q[j]=q[i]
                q[i]=s1



minimumBribes(q)



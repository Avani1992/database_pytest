import os
import sys
import json
"""
we have to differenciate the magical and non-magical word from the list and store in in dictionary form and write it in json file
"""
class magicalword_json:
    L= ['aXX','aaHaa','IIhIIO','AAsAA','9I9','..R..','@@h@@@@','DDcDD','223221','***8***']
    l1=list()
    for i in L:
       if(len(i)%2!=0):
           l1.append(i)

    print(l1)

    magic_list=list(filter(lambda x:x+str(1),l1))
    print(magic_list)
    l2=list()
    l3=list()
    d=dict()
    for i in L:
        len1=int(len(i)/2)
        front=i[0:len1]
        back=i[(len1+1):]
        # print("front:",front)
        # print("rever: ",list(reversed(back)))
        if(list(front)==list(reversed(back))):
            l2.append(i)
        else:
            l3.append(i)
    print("Magic:",l2)
    print("nonmagic:",l3)
    d["Magic_word"]=l2
    d["Non-magicword"]=l3
    with open("magic_nonmagic.json","w") as file1:
        json.dump(d,file1)
        file1.close()


        # with open("magic_nonmagic.json", "a") as File1:
        #         json.dump(d,File1)
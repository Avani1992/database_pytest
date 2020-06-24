"""In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left."""


def count_substring(string, sub_string):
    l=0
    counter=0

    while(l<len(string)):
        p=0
        s1=string[l:]
        print(s1)
        if(sub_string in s1):
            p=s1.index(sub_string)
            print(p)

            counter=counter+1
            print(counter)
        l = p + len(sub_string)
        print(l)




    return counter

result=count_substring('I am an Indian, birth by  birth .','birth')
print(result)
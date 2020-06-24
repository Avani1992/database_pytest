
string='ABCDCDCDC'
sub_string='CDC'
def count_substring(string, sub_string):
    counter=0
    l1=len(sub_string)
    for i in range(0,len(string)):
        if(sub_string in string[i:(i+l1)]):
                counter=counter+1

    return (counter)

count = count_substring(string, sub_string)
print(count)
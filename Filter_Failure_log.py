import os
import sys

class Filter_Failure_log:
    with open('failure_wp.log','r') as file1:
           data=file1.readlines()
           t = [i[:-1] for i in data]
           data = t
           file1.close()
    #print(data)
    def filter_file(self):
        filter_list=list(filter(lambda x:  ('~' in x),Filter_Failure_log.data))
        print("Lines in which '~' character is: ",(filter_list))
obj=Filter_Failure_log()
obj.filter_file()
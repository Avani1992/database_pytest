import sys
import os

class filter_dict:

    def filter_dict1(self,dict2):
      filter_dict=dict(filter(lambda x : (("True" in x) or ("False" in x)),dict2.items()))
      print(filter_dict)

      for i in filter_dict.keys():
        print(i)
dict2={ 1:1, 2:"True", 3:"False", 4:3, 5:'I', 6:"True"}
obj=filter_dict()
obj.filter_dict1(dict2)



import subprocess
import pytest


# txt = "Save to clipboard!!!!!"
# subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), ccmdheck=True)


d1 = {"Roti": {"1": "Plain", "2": "Naan", "3": "Parotha", "4": "Chapati"}}
unpacked = d1["Roti"]["3"]

data={"Menu": ["Roti","Sabji","Salad","South-Indian","Dessert"],
  "Roti": {"1": "Plain", "2": "Naan", "3": "Parotha", "4": "Chapati"},
  "Sabji": {"1": "SevTomato", "2": "Onion", "3": "Gobi", "4": "Paneer"},
  "Salad": {"1": "Italian", "2": "Green", "3": "Corn", "4": "Brokli"},
  "South-Indian": {"1": "Dosa", "2": "Idly", "3": "Vada", "4": "Upma"},
  "Dessert": {"1": " GulabJamun", "2": "Ice-Cream", "3": "Lassi", "4": " Rasgulla"}}
s1=dict()
a="FastFood"
te = 'Brokli'

for ele in data.values():
   if type(ele) != list:
    #if te in ele.values():
  #     keys = list(ele.keys())
  #     vals = list(ele.values())
  #     ind = vals.index(te)
  #     key1= keys[ind]

      print(ele.values())

# for i in range(1, len(data["Menu"])+1):
#     s1[i] = data["Menu"][str(i)]
# print(len(s1))
# s1[str(len(s1)+1)]=a
# data["Menu"]=s1[str(len(s1)+1)]
# print(data["Menu"])

# print(data["Menu"])

# import copy
#
# MenuVal = copy.deepcopy(data["Menu"])
# print(type(MenuVal))
# MenuVal['6'] = a      # if key is not there then it will create a new key
# print(MenuVal)
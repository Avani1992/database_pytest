import os
import sys
import json

class Eassay_json:
    with open("Essay.json","r") as File2:
       data=json.load(File2)
    print(data)
    File2.close()
    def Essay1(self):

        self.s2=""
        self.s3=""
        for i,j in Eassay_json.data.items():
            for k,l in j.items():
                if(i=='Animal'):
                  if(k=='place'):
                    self.s2=self.s2 +" "+ i +" "+ "lives in" +" "+ l+"."+"\n"
                  else:
                    self.s2=self.s2 +" "+ i +" "+ k +" "+ "is" +" "+ str(l)+"."+"\n"
                elif(i=='Animal1'):

                    if (k == 'place'):
                        self.s3 = self.s3 + " " + "Animal" + " " + "lives in" + " " + l + "." + "\n"
                    else:
                        self.s3 = self.s3 + " " + "Animal" + " " + k + " " + "is" + " " + str(l) + "." + "\n"

    def print1(self):
        File1= open("1.txt","w+")
        File1.write("Essay on Dog :\n")
        File1.write("**************************\n")
        File1.writelines(self.s2)
        File1.write("**************************\n")
        File1.write("Essay on Tiger :\n")
        File1.write("**************************\n")
        File1.writelines(self.s3)
        File1.close()

            # do not use JSON library to dump data into text file ...use smething else
        print(self.s2)



obj1=Eassay_json()
obj1.Essay1()
obj1.print1()




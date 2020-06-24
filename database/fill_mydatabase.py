"""Problem Statement: Fill one live webserver Database with thousand user data.
Every user is containing five different properties.
Expected output: Database should be filled with one thousand different user with five different properties(Fake).
Three file:  fill_mydatabase.py , test_data.py and Logging12.py and Logging.log.
"""

import mysql.connector
from random import *
import logging
from Logging12 import *


class fill_mydatabse:

    def create_table(self):
        self.con = mysql.connector.connect(host="localhost", username="root", password="user123", database="employee_detail")
        self.cursor=self.con.cursor()
        # self.cursor.execute("Create table employee_data(emp_id integer,emp_name varchar(45),emp_email varchar(45),emp_salary double,emp_gender varchar(45),emp_city varchar(45)) ")
        # self.con.commit()

    def fill_data(self):


        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        self.gender=""
        self.city=""
        for i in range(1,1001):
            self.q1="insert into employee_data(emp_id,emp_name,emp_email,emp_salary,emp_gender,emp_city) values(%s,%s,%s,%s,%s,%s)"
            l1 = ["Male","Female"]
            l2=["Mumbai","Bangalore","Pune","Ahmedabad","Chennai","Hyderabad"]
            self.gender=choice(l1)
            self.city=choice(l2)
            if(i<50):
                self.values=(i,"user"+str(i),"user"+str(i)+"@gmail.com",i*1000,self.gender,self.city)
                self.cursor.execute(self.q1, self.values)
                self.con.commit()
                logging.info(self.values)

            elif(i<70):
                self.values = (i, "user" + str(i), "user" + str(i) + "@gmail.com", i * 900, self.gender, self.city)
                self.cursor.execute(self.q1, self.values)
                self.con.commit()
                logging.info(self.values)

            else:
                self.values = (i, "user" + str(i), "user" + str(i) + "@gmail.com", i * 500, self.gender, self.city)
                self.cursor.execute(self.q1, self.values)
                self.con.commit()
                logging.info(self.values)

        self.con.close()





            
        
obj=fill_mydatabse()
obj.create_table()
obj.fill_data()

import os
import sys
import mysql.connector

class test_database2:
    def test(self,a):
        self.db=mysql.connector.connect(host="localhost",user="root",passwd="user123",database="DATA_MENU")
        self.cursor=self.db.cursor()
        #self.cursor.execute("CREATE DATABASE DATA_MENU")
        self.query="CREATE TABLE MENU(Roti varchar(255),Sabji varchar(255))"
        #self.cursor.execute(self.query)
        #self.query1="INSERT INTO menu_data1(name) VALUES(%s)"
        #self.values=[[("Plain")],[("Naan")],[("Paratha")],[("Chapati")]]
        self.values=[[("Roti")],[("Sabji")]]
        #self.cursor.executemany(self.query1,self.values)
        #self.name = (a[1])
        # self.query2 = "ALTER TABLE menu_data1 ADD COLUMN "+self.name+" VARCHAR(255)"
        # #
        # #
        # self.cursor.execute(self.query2)
        # self.q1="CREATE TABLE "+ self.name+ "(name varchar(255),price varchar(5))"
        # self.cursor.execute(self.q1)
        # self.query3 = "INSERT INTO " + self.name + "(name,price) VALUES(%s,%s)"
        # self.l1 = a[2].split(",")
        # print(self.l1)
        # self.values=list()
        # self.i=0
        # for j in range(self.i, len(self.l1)):
        #       self.l2=self.l1[j].split(":")
        #       self.values.append(tuple(self.l2))
        #
        #
        #
        # #self.values=[("Corn","2"),("Corn3","8")]
        # #print(self.values)
        # #self.cursor.executemany(self.query3,self.values)
        #self.q3="ALTER TABLE Menu DROP " +self.name
        #self.cursor.execute(self.q3)
        self.query3 = "SELECT * FROM menu_data1"
        self.cursor.execute(self.query3)
        self.data = self.cursor.fetchall()
        # print(self.records)
        self.l1 = list()
        for data in self.data:
             self.s1 = ''.join(data)
             self.l1.append(self.s1)
        print(self.l1)
        self.q4="CREATE TABLE menu_data5(name varchar(255),quan varchar(45))"
        #self.cursor.execute(self.q4)
        self.q5="INSERT INTO menu_data5(name,quan) VALUES(%s,%s)"
        self.s1=""
        t=input("Enter type:")
        self.s1=self.s1+t
        t1=input("Enter price:")
        self.s2=""
        self.s2=self.s2+t1
        self.values=[self.s1,self.s2]
        #self.cursor.execute(self.q5,self.values)
        #

        self.db.commit()
        self.q1 = "SELECT name,quan FROM menu_data5"
        self.cursor.execute(self.q1)
        self.data = self.cursor.fetchall()
        self.l2 = list()
        self.l3=list()
        for data in self.data:
            self.s1 = ''.join(data[0:1])
            self.s2=''.join(data[1:])
            self.l2.append(self.s1)
            self.l3.append(self.s2)
        print( self.l2)
        print(self.l3)
        t=input("type: ")
        print(t)
        self.q2="SELECT quan FROM menu_data5 WHERE name=%s"
        #self.cursor.execute(self.q2,(t,))
        #self.data1=self.cursor.fetchall()
        #print(self.data1)
        self.t1="Salad"
        self.q3="delete from menu_data5 where name=%s"
        self.cursor.execute(self.q3,(t,))
        self.db.commit()




obj=test_database2()
obj.test(sys.argv)
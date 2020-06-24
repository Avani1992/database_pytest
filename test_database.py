import sys
import os
import mysql.connector

class test_database:
    def test(self,a):
        self.conn=mysql.connector.connect(host="localhost",user="root",passwd="user123",database="DATA2")
        self.cursor=self.conn.cursor()
        # self.query="CREATE DATABASE DATA2"
        # self.cursor.execute(self.query)
        self.a=a[1]
        print(self.a)
        #self.query1="CREATE TABLE DATA(roti varchar(255))"

        #self.cursor.execute(self.query1)
        self.query2="ALTER TABLE DATA ADD COLUMN Sabji VARCHAR(255)"
        self.values=[a[1]]
        self.cursor.execute(self.query2)
        self.query3="SELECT * FROM DATA"
        self.cursor.execute(self.query3)
        self.records=self.cursor.fetchall()
        print(self.records)
        self.conn.commit()
        print("Data added")
obj=test_database()
obj.test(sys.argv)
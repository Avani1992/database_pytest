import mysql.connector

import  json

class key_test:

    def create_table(self):
        self.con = mysql.connector.connect(host="localhost", username="root", password="user123", database="key_test")
        self.cursor=self.con.cursor()
       # self.cursor.execute("create table Customers(cu_id int not null,cu_name varchar(45),roti varchar(45),sabji varchar(45),sweet varchar(45),primary key(cu_id))")
       # self.cursor.execute("Create table orders(or_id int not null, o_name varchar(45), cu_id int not null ,primary key(or_id),foreign key(cu_id) references Customers(cu_id))")


        self.con.commit()

    def fill_data(self):

        # self.q1="insert into Customers(cu_id,cu_name,roti,sabji,sweet) values(%s,%s,%s,%s,%s)"
        # self.values=[(1001,"Kuman","Plain","brinjal","Gulab-Jamun"),(1003,"Avani","Fulka","Paneer","Rasgulla"),(1002,"Ruchi","Naan","PaneerBhurji","Rasmalai"),
        #              (1005,"Pooja","Plain","Tomato","Barfi"),(1007,"Neha","Tanduri","Potato","Jamun")]
        # self.cursor.executemany(self.q1,self.values)

        # self.q2="insert into orders(or_id,o_name,cu_id) values(%s,%s,%s)"
        # self.values=[(101,"order1",1001),(102,"order3",1003),(103,"order2",1005),(104,"order4",1003),(105,"order5",1002),(106,"order6",1007)]
        # self.cursor.executemany(self.q2,self.values)
        # self.con.commit()

        self.q3="select * from Customers"
        self.cursor.execute(self.q3)
        self.data=self.cursor.fetchall()
        print(self.data)
        with open("customeres_data.json","w") as file1:
            self.l2 = list()
            self.d1 = dict()
            for data in self.data:
                self.d1[data[0]]=data
            file1.write(json.dumps(self.d1))
            print(self.d1)






obj=key_test()
obj.create_table()
obj.fill_data()

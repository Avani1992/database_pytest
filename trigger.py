import mysql.connector

class trigger:
    def read_file(self):
        self.db=mysql.connector.connect(host="localhost",user="root",passwd="user123",database="TEST")
        self.cursor=self.db.cursor()
        #self.cursor.execute("CREATE DATABASE TEST")

        self.q1="CREATE TABLE STUDENT(stu_ID int(6) NOT NULL UNIQUE,name VARCHAR(10) NOT NULL,sub_1 int(10),sub_2 int(10),Total int(20),PRIMARY KEY(stu_Id))"
        #self.cursor.execute(self.q1)
        self.q2="CREATE TABLE Stu_detail(name VARCHAR(10), Total int(10))"
        #self.cursor.execute(self.q2)
        self.t1="CREATE TRIGGER Stu_marks BEFORE INSERT ON STUDENT FOR EACH ROW SET new.Total=new.sub_1 + new.sub_2"
        #self.cursor.execute(self.q2)
        self.q3="INSERT INTO STUDENT VALUES(3,'RUCHI',30,30,0)"
        #self.cursor.execute(self.q3)
        self.t2="CREATE TRIGGER Stu_status AFTER INSERT ON Stu_detail FOR EACH ROW UPDATE STUDENT SET Total='Pass'"
        #self.cursor.execute(self.t2)
        self.q4="INSERT INTO Stu_detail VALUES('AVANI',30)"
        self.cursor.execute(self.q4)
        self.db.commit()
obj=trigger()
obj.read_file()
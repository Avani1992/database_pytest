
import pytest
import mysql.connector


class Tests_A():
    def test_emp_data(self,test_con2):
        self.q1=test_con2[1].execute("select * from emp_data")
        self.data=test_con2[1].fetchall()
        print(self.data)

    def demo(self):
        print("Hello...")

obj=Tests_A()
obj.demo()



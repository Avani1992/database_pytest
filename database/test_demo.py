import pytest
import mysql.connector

expected_result=[("Avani",28),("Kuman",29),("Pooja",21)]
def test_emp_data(test_con2):
    for i in range(1,3):
        j="Avani"
        q1 = "select * from emp_data where name=%s"
        test_con2[1].execute(q1,(j,))
        data = test_con2[1].fetchall()
        print(data)
        #assert (data==expected_result)
        print("passed......")



# def test_TC_DB_02_insert_quert_validate(test_con2):
#     q1="insert into emp_data (Name,Age) values(%s,%s)"
#     values = (["Avani",28], ["Kuman",29], ["Ruchi",21])
#     test_con2[1].executemany(q1,values)
#     test_con2[0].commit()
#     print("Data inserted...")

#
# def test_TC_DB_03_update_query_validate(test_con2):
#     q1="update emp_data set Name=%s where Age=%s"
#     values=[("Pooja",21)]
#     test_con2[1].executemany(q1,values)
#     test_con2[0].commit()
#     print("Data Updated...")

# def test_TC_DB_04_select_Name_Age_query(test_con2):
#     test_con2[1].execute("select Name from emp_data")
#
#     data=test_con2[1].fetchall()
#
#     for name in data:
#         s1=''.join(name)
#         print(s1)
#
#     test_con2[1].execute("select Age from emp_data")
#     data1=test_con2[1].fetchall()
#
#     for age in data1:
#
#         print(age)

# #
# def test_TC_DB_05_Delete_query_Validate(test_con2):
#     test_con2[1].execute("delete from emp_data")
#     test_con2[0].commit()
#     print("Data deleted...")
"""compare the logfile data and database data to check both are same or not. If both are same then test Passed else test failed."""
import mysql.connector
from random import *


def test_data(test_con2):
    
    for i in range(1, 3):
        data=""
        a_file = open("Logging.log")
        j = choice(range(1, 500))

        lines_to_read = [j-1]
        
        for position, line in enumerate(a_file):  # check for position and line at that position.
             if position in lines_to_read:
                 print(" Log file data: ",line) # string form.
                     
        # q2 = "SELECT * FROM employee_data WHERE emp_id=%s"
        # test_con2[1].execute(q2, (str(j),))
        # data = test_con2[1].fetchall()
        
        s1="user"+str(j)
        q2 = "SELECT * FROM employee_data WHERE emp_name=%s"
        test_con2[1].execute(q2, (s1,))
        data = test_con2[1].fetchall()
        for data1 in data:
            s1=''.join(str(data1)) # convert to string.
            print("Database data: ",s1)
        
        if(line.find(s1)):
            print("Data Matched...")
        else:
            print("Wrong data...")

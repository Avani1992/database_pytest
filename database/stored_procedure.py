import mysql.connector

# def procedure4():
#     try:
#         con = mysql.connector.connect(host="localhost", username="root", password="user123", database="key_test")
#         cursor=con.cursor()
#         args=[974,0]
#
#         result=cursor.callproc('if_else_then',args)  # for single row output.
#
#         print(result[1])
#     except mysql.connector.Error as error:
#         print("Failed to execute stored procedure: {}".format(error))
#
#     finally:
#         if (con.is_connected()):
#             cursor.close()
#             con.close()
#         print("MySQL connection is closed")
#
#
# procedure4()

#2.

def procedure5():
    try:
        con = mysql.connector.connect(host="localhost", username="root", password="user123", database="key_test")
        cursor = con.cursor()
        args = ['1003']

        cursor.callproc('mul_procedure',args)
        for result in cursor.stored_results():       # for multiple row  output.
            print(result.fetchall())


    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
        print("MySQL connection is closed")

procedure5()
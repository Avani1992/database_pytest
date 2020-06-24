import mysql.connector
from random import *
import  json


def test_data(test_con2):
    
    with open("customeres_data.json","r") as file1:
        data=json.load(file1)  # read data from json file...it;s in dictionary form
        #print(data)
        
    l1=["order1","order2","order3","order4","order5","order6"]
    q1="select cu_id from orders where o_name=%s"
    order=choice(l1)  # select order no.
    print("orderNo=",order)
    test_con2[1].execute(q1,(order,))
    id=test_con2[1].fetchall()  # fetch cu_id.
    #print("id: ",id)
    cu_id=id[0][0]  
    print("cu_id=",cu_id)
    q2="select * from customers where cu_id=%s"
    test_con2[1].execute(q2,(str(cu_id),))  # fetch data from DB according cu_id.
    cu_data=test_con2[1].fetchall()
    print("cu_data= ",cu_data)
    
    json_data=tuple(data[str(cu_id)])  # fetch data from json file accordingly cu_id in tuple form.
    print("json_data=" ,json_data)
    
    if(cu_data[0]==json_data):
        print("Data matched....")
    
    file1.close()  # close the file..
    test_con2[0].close()
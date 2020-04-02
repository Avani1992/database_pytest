import pytest
import mysql.connector
# Create connection and Cursor object for using it in query.
@pytest.fixture
def test_con2():
    con = mysql.connector.connect(host="localhost", username="root", password="user123", database="key_test")
    # if (self.con.connect):
    #     print("Yes")
    cursor=con.cursor()

    return [con,cursor]
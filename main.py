# main.py
from database_connection import get_connection
from my_package.effects import effect
from my_package.filters import filter
from my_package.filters import filter1
from test_modules import abc as abcFunc # WHEN NO __INIT__ * WONT WORK
from test_modules import * # THIS NOW WORKS BECAUSE IT HAVE __INIT__ WITH __ALL__ SET TO abc and test
# import sys
# sys.path.insert(0,r'C:\Users\kevin.mensah\Desktop\python') # INSERT PATH INTO BEGINNING OF SYS.PATH
# sys.path.append(r'C:\Users\kevin.mensah\Desktop\python') # APPEND PATH TO END OF SYS.PATH
# from test_modules import test
# print(test.test())
peoples: list[str] = ["Kevin", "Rojenson","Rustian","Arween", "John Paul", "John Floyd"]

filteredPeople: list[str] = [people for people in peoples if len(people) > 7 ]


def main():
    print(f"{filteredPeople}, filteredPeople")
    abc.abc()
    test.test()
    # print(effect.effect())
    # print(filter1.filter1())
    # Get the database connection
    conn = get_connection()
    if conn is not None:
        try:
            # Create a cursor object
            cursor = conn.cursor()
            
            # Execute a query
            cursor.execute("SELECT version();")
            
            # Fetch the result
            db_version = cursor.fetchone()
            print(f"Database version: {db_version}")
            
            # Close the cursor
            cursor.close()
            
        except Exception as error:
            print(f"Error executing query: {error}")
        finally:
            # Close the connection
            conn.close()

if __name__ == "__main__":
   
    main()

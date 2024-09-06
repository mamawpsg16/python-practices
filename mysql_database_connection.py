import mysql.connector

database_config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database":"sql_practice"
}
def database_connection():
    cnx = mysql.connector.connect(**database_config)
    try:
        cursor = cnx.cursor()
        cursor.execute("""
            select * from customers
        """)
        result = cursor.fetchall()
        print(result,"result")
    finally:
        cnx.close()